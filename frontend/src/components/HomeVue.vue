<script setup lang="ts">
import { ref } from "vue";
import axios from "axios";

const page = ref("login");
const tokens = ref("");
const secret = ref("");
const message = ref("");
const server = "http://localhost:5000";
const history = ref([] as string[]);

async function login() {
  const response = await axios.get(`${server}/login`, {
    headers: {
      Authorization: "Bearer " + secret,
    },
  });
  const status = response.status;

  if (status === 200) {
    page.value = "gigachat";
  } else {
    alert("Wrong Secret");
  }
}

async function gigachat() {
  history.value.push(message.value);

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
    history.value.push(answer);
  } else {
    page.value = "login";
    alert("Wrong Secret");
  }
}
</script>

<template>
  <div class="container">
    <div v-if="page === 'gigachat'" id="gigachat">
      <p class="fs-3 text-center mb-3">GigaChat</p>
      <p class="fs-5 text-right">Tokens
        <span class="badge bg-primary">{{ tokens }}</span>
      </p>
      <button class="btn btn-danger" @click="page = 'login'">Logout</button>
      <div>
        <div v-for="message in history">{{ message }}</div>
        <form @submit.prevent="gigachat">
          <input class="form-control" type="text" v-model="message" placeholder="Type your promt" />
          <button class="btn btn-primary" type="submit">Send</button>
        </form>
        <button class="btn btn-warning" @click="history = []; message = ''">Clear</button>
      </div>
    </div>

    <div v-else id="login">
      <p class="fs-3 text-center mb-3">Login</p>
      <form class="form-inline justify-content-center mb-3" @submit.prevent="login">
        <input class="form-control" type="text" v-model="secret" placeholder="Enter Client Secret" />
        <button class="btn btn-primary" type="submit">Submit</button>
      </form>
    </div>
  </div>
</template>

<style scoped>
#login {
  max-width: 500px;
  margin: 0 auto;
}
#gigachat {
  max-width: 500px;
  margin: 0 auto;
}
</style>