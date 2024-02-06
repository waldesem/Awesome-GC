<script setup lang="ts">
import { GigaStore } from "../actions";

const storeGiga = GigaStore();

const models: string[] = [];
</script>

<template>
  <div class="container">
    <div id="gigachat">
      <div class="justify-content-center">
        <p class="fs-3 text-center mb-3">SberGigaChat</p>
        <div class="mb-3 row">
          <label class="col-form-label" for="models">Models</label>
          <div class="col-auto">
            <select class="form-select" required name="models"
                    v-model="storeGiga.GigaStore.model">
              <option v-for="item, index in models" :key="index"
                      :value="item">{{item}}
              </option>
            </select>
          </div>
        </div>
        <div id="history" class="text-start mb-3">
          <div class="mb-3" v-for="(item, index) in storeGiga.GigaStore.history" :key="index">
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
        <form class="mb-3" @submit.prevent="gigachat">
          <textarea
            class="form-control"
            v-model="storeGiga.GigaStore.message"
            placeholder="Type your question"
          ></textarea>
          <div class="btn-group mt-3 d-flex" role="group">
            <button :disabled="storeGiga.GigaStore.spinner" class="btn btn-primary" type="submit">
              Send
              <span
                v-if="storeGiga.GigaStore.spinner"
                class="spinner-border spinner-border-sm"
              ></span>
            </button>
            <button
              class="btn btn-secondary"
              @click="
                storeGiga.GigaStore.history = [];
                storeGiga.GigaStore.message = '';
                storeGiga.GigaStore.spinner = false;
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
