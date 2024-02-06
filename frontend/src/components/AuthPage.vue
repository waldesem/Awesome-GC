<script setup lang="ts">
import { ref } from "vue";
import { GigaStore } from "../actions";
import router from "../router";

const storeGiga = GigaStore();

const visible = ref(false);
</script>

<template>
  <div class="container">
    <div id="auth">
      <div class="row justify-content-center">
        <p class="fs-3 text-center mb-3">SberGigachat</p>
        <div v-if="storeGiga.ChatObj.typo === 'auth'">
          <form
            class="row mb-3 text-center"
            @submit.prevent="router.push({ name: 'gigachat' })"
          >
            <div class="col-auto">
              <div class="input-group">
                <input
                  class="form-control"
                  type="password"
                  required
                  v-model="storeGiga.ChatObj.secret"
                  placeholder="Enter Authorization Key"
                />
                <span class="input-group-text">
                  <a role="button" @click="visible = !visible">
                    {{ "Hide" ? visible : "Show" }}
                  </a>
                </span>
              </div>
            </div>
            <div class="col-auto">
              <button class="btn btn-primary" type="submit">Submit</button>
            </div>
          </form>
        </div>

        <div v-else>
          <form
            class="mb-3 text-center"
            @submit.prevent="router.push({ name: 'gigachat' })"
          >
            <input
              class="form-control"
              type="text"
              required
              v-model="storeGiga.ChatObj.logopass.username"
              placeholder="Enter username"
            />
            <div class="input-group">
              <input
                class="form-control"
                type="password"
                required
                v-model="storeGiga.ChatObj.logopass.password"
                placeholder="Enter password"
              />
              <span class="input-group-text">
                <a role="button" @click="visible = !visible">
                  {{ "Hide" ? visible : "Show" }}
                </a>
              </span>
            </div>
            <button class="btn btn-primary" type="submit">Submit</button>
          </form>
        </div>

        <div>
          <button
            class="btn btn-secondary"
            type="button"
            @click="
              storeGiga.ChatObj.typo = 'auth'
                ? storeGiga.ChatObj.typo === 'logopass'
                : 'auth'
            "
          >
            {{
              "Enter with login and password"
                ? storeGiga.ChatObj.typo === "logopass"
                : "Enter with authorization data"
            }}
          </button>
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
