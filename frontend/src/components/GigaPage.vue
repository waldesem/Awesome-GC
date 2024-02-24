<script setup lang="ts">
import axios from "axios";
import { computed, ref } from "vue";

interface ChatMessage {
  sender: string;
  message: string;
}

interface LogoPass {
  username: string;
  password: string;
}

// const server = "http://localhost:8000";
const server = "";

const chatObj = ref({
  visible: false,
  typo: "auth",
  secret: "",
  logopass: <LogoPass>{
    username: "",
    password: "",
  },
  message: "",
  spinner: false,
  model: "",
  models: ["GigaChat", "GigaChat-Plus", "GigaChat-Pro"],
  history: <ChatMessage[]>[
    { sender: "Gigachat", message: "Hello, how can I help you?" },
  ],

  gigachat: async function () {
    this.spinner = true;
    this.history.push({ sender: "You", message: this.message });
    const element = document.getElementById("history");
    element?.scrollTo(0, 9999999999999999999999);
    try {
      const response = await axios.post(`${server}/gigachat/${this.typo}`, {
        model: this.model,
        question: this.message,
        auth: this.secret,
        login: this.logopass,
      });
      console.log(response.status);
      this.message = "";
      const { answer } = response.data;
      this.history.push({ sender: "Gigachat", message: answer });
      element?.scrollTo(0, 9999999999999999999999);
    } catch (error) {
      console.log(error);
      chatObj.value.typo = "auth";
      alert("Something went wrong. Check authorization data or retry later");
    }
    this.spinner = false;
  },
});

const selectedModel = computed(() => {
  return chatObj.value.models[0];
});
</script>

<template>
  <div class="container">
    <div class="row justify-content-center">
      <div v-if="chatObj.typo !== 'gigachat'" id="auth">
        <p class="fs-3 text-center mb-3">SberGigaLogin</p>
        <form class="mb-3" @submit.prevent="chatObj.typo = 'gigachat'">
          <div v-if="chatObj.typo === 'auth'" class="mb-3">
            <div class="input-group">
              <input
                class="form-control"
                :type="chatObj.visible ? 'text' : 'password'"
                autocomplete="current-password"
                required
                v-model="chatObj.secret"
                placeholder="Enter Authorization Key"
              />
              <span class="input-group-text">
                <a role="button" @click="chatObj.visible = !chatObj.visible">
                  {{ chatObj.visible ? "Hide" : "Show" }}
                </a>
              </span>
            </div>
          </div>

          <div v-else class="mb-3">
            <div class="mb-3">
              <input
                class="form-control mb-3"
                type="text"
                required
                v-model="chatObj.logopass.username"
                placeholder="Enter username"
              />
              <div class="input-group mb-3">
                <input
                  class="form-control"
                  :type="chatObj.visible ? 'text' : 'password'"
                  autocomplete="current-password"
                  required
                  v-model="chatObj.logopass.password"
                  placeholder="Enter password"
                />
                <span class="input-group-text">
                  <a role="button" @click="chatObj.visible = !chatObj.visible">
                    {{ chatObj.visible ? "Hide" : "Show" }}
                  </a>
                </span>
              </div>
            </div>
          </div>

          <div class="d-grid gap-2 mb-3">
            <button class="btn btn-primary" type="submit">Submit</button>
          </div>
        </form>

        <div class="mb-3">
          <a
            class="btn btn-link"
            role="button"
            type="button"
            @click="
              chatObj.typo = chatObj.typo === 'auth' ? 'logopass' : 'auth'
            "
          >
            {{
              chatObj.typo === "auth"
                ? "Enter with login/password"
                : "Enter with authorization data"
            }}
          </a>
          <a
            class="btn btn-link"
            href="https://developers.sber.ru/docs/ru/gigachat/api/integration"
            target="_blank"
            >Подключение API</a
          >
        </div>
        <p class="fw-light text-danger text-center">
          Nothing data not be saved on server
        </p>
      </div>

      <div v-if="chatObj.typo === 'gigachat'" id="gigachat">
        <p class="fs-3 text-center mb-3">SberGigaChat</p>
        <div class="mb-3 row">
          <select
            class="form-select"
            name="models"
            v-model="selectedModel"
          >
            <option
              v-for="(item, index) in chatObj.models"
              :key="index"
              :value="item"
            >
              {{ item }}
            </option>
          </select>
        </div>
        <div id="history" class="text-start mb-3">
          <div
            class="mb-3"
            v-for="(item, index) in chatObj.history"
            :key="index"
          >
            <div
              class="bg-opacity-75 border rounded text-wrap text-light p-3 mb-2"
              :class="`bg-${
                Object.values(item)[0] === 'Gigachat' ? 'primary' : 'success'
              }`"
            >
              {{ `${Object.values(item)[0]}: ${Object.values(item)[1]}` }}
            </div>
          </div>
        </div>
        <form class="mb-3" @submit.prevent="chatObj.gigachat">
          <textarea
            class="form-control"
            required
            v-model="chatObj.message"
            placeholder="Type your question"
          ></textarea>
          <div class="btn-group mt-3 d-flex" role="group">
            <button
              :disabled="chatObj.spinner"
              class="btn btn-primary"
              type="submit"
            >
              Send
              <span
                v-if="chatObj.spinner"
                class="spinner-border spinner-border-sm"
              ></span>
            </button>
            <button
              class="btn btn-secondary"
              type="reset"
              @click="
                chatObj.history = [];
                chatObj.message = '';
                chatObj.spinner = false;
              "
            >
              Clear
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<style scoped>
#auth {
  max-width: 50vh;
  margin: 0 auto;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: #f8f8f8;
  margin-top: 50px;
  margin-bottom: 50px;
  padding: 20px;
}
#gigachat {
  max-width: 75vh;
  min-height: 50vh;
  margin: 0 auto;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: #f8f8f8;
  margin-top: 50px;
  margin-bottom: 50px;
  padding: 20px;
}
#gigachat #history {
  height: 600px;
  overflow-y: scroll;
}
</style>
