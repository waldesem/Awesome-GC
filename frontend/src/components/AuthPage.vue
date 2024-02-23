<script setup lang="ts">
import { ref } from "vue";
import { router } from "../router";

const loginObj = ref({
  visible: false,
  typo: "auth",
  secret: "",
  username: "",
  password: "",

  submitForm: function () {
    if (this.typo === "logopass") {
      localStorage.setItem("gigachattypo", "logopass");
      localStorage.setItem("gigachatusername", this.username);
      localStorage.setItem("gigachatpassword", this.password);
    } else {
      localStorage.setItem("gigachattypo", "auth");
      localStorage.setItem("gigachatsecret", this.secret);
    }
    router.push({ name: "gigachat" });
  },

  switchForm: function () {
    this.typo = this.typo === "auth" ? "logopass" : "auth";
  },
});
</script>

<template>
  <div class="container">
    <div id="auth">
      <div class="row justify-content-center">
        <p class="fs-3 text-center mb-3">SberGigachat</p>
        <div v-if="loginObj.typo === 'auth'">
          <form
            class="mb-3"
            @submit.prevent="router.push({ name: 'gigachat' })"
          >
            <div class="mb-3">
              <div class="input-group">
                <input
                  class="form-control"
                  :type="loginObj.visible ? 'text' : 'password'"
                  autocomplete="current-password"
                  required
                  v-model="loginObj.secret"
                  placeholder="Enter Authorization Key"
                />
                <span class="input-group-text">
                  <a
                    role="button"
                    @click="loginObj.visible = !loginObj.visible"
                  >
                    {{ loginObj.visible ? "Hide" : "Show" }}
                  </a>
                </span>
              </div>
            </div>
            <div class="d-grid gap-2 mb-3">
              <button class="btn btn-primary" type="submit">Submit</button>
            </div>
          </form>
        </div>

        <div v-else>
          <form
            class="mb-3"
            @submit.prevent="router.push({ name: 'gigachat' })"
          >
            <input
              class="form-control mb-3"
              type="text"
              required
              v-model="loginObj.username"
              placeholder="Enter username"
            />
            <div class="input-group mb-3">
              <input
                class="form-control"
                :type="loginObj.visible ? 'text' : 'password'"
                autocomplete="current-password"
                required
                v-model="loginObj.password"
                placeholder="Enter password"
              />
              <span class="input-group-text">
                <a role="button" @click="loginObj.visible = !loginObj.visible">
                  {{ loginObj.visible ? "Hide" : "Show" }}
                </a>
              </span>
            </div>
            <div class="d-grid gap-2 mb-3">
              <button class="btn btn-primary" type="submit">Submit</button>
            </div>
          </form>
        </div>

        <div>
          <a class="btn btn-link" type="button" @click="loginObj.switchForm">
            {{
              loginObj.typo === "auth"
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
</style>
