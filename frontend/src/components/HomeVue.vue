<script setup lang="ts">
import { ref } from "vue";
import axios from "axios";

interface ChatMessage {
  sender: string;
  message: string;
}

const page = ref("login");
const secret = ref("");
const message = ref("");
const spinner = ref(false);
// const server = "http://localhost:5000";
const server = "";
const history = ref<ChatMessage[]>([{ sender: "Gigachat", message: "Hello, how can I help you?" }]);

async function login() {
  if (secret.value) {
    page.value = "gigachat";
  } else {
    alert("Wrong Secret");
  }
}

async function gigachat() {
  history.value.push({ sender: "You", message: message.value });
  spinner.value = true;
  const element = document.getElementById("history");
  element?.scrollTo(0, 9999999999999999999999);
  const response = await axios.post(
    `${server}/gigachat`,
    {
      promt: message.value,
    },
    {
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + secret.value,
      },
    }
  );
  const status = response.status;

  if (status === 201) {
    const { answer } = await response.data;
    history.value.push({ sender: "Gigachat", message: answer });
    element?.scrollTo(0, 9999999999999999999999);
    message.value = "";
  } else {
    page.value = "login";
    alert("Wrong Secret");
  }
  spinner.value = false;
}
</script>

<template>
  <div class="container">
    <div v-if="page === 'gigachat'" id="gigachat">
      <div class="justify-content-center">
        <p class="fs-3 text-center mb-3">SberGigaChat</p>
        <div id="history" class="text-start mb-3">
          <div class="mb-3" v-for="item, index in history" :key="index">
            <div class="bg-opacity-75 border rounded text-wrap text-light p-3 mb-2" 
                :class="`bg-${Object.values(item)[0] === 'Gigachat' ? 'primary' : 'success'}`">
              {{ `${Object.values(item)[0]}: ${Object.values(item)[1]}` }}
            </div>
          </div>
        </div>
        <form class="mb-3" @submit.prevent="gigachat">
          <textarea class="form-control" v-model="message" placeholder="Type your promt"></textarea>
          <div class="btn-group mt-3 d-flex" role="group">
            <button :disabled="spinner" class="btn btn-primary" type="submit">Send
              <span v-if="spinner" class="spinner-border spinner-border-sm"></span>
            </button>
            <button class="btn btn-secondary" @click="history = []; message = ''; spinner = false">Clear</button>
          </div>
        </form>
      </div>
    </div>

    <div v-else id="login">
      <div class="row justify-content-center">
        <p class="fs-3 text-center mb-3">SberGigachat</p>
        <form class="row mb-3 text-center" @submit.prevent="login">
          <div class="col-auto">
            <input class="form-control" type="text" v-model="secret" placeholder="Enter Authorization Key" />
          </div>
          <div class="col-auto">
            <button class="btn btn-primary" type="submit">Submit</button>
          </div>
        </form>
        <div>
          <a class="btn btn-link" href="https://developers.sber.ru/docs/ru/gigachat/api/integration" target="_blank">Подключение API</a>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
#login {
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
  max-width: 50vh;
  min-height: 75vh;
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
  height: 800px;
  overflow-y: scroll;
}
</style>