<script setup lang="ts">
import { defineAsyncComponent } from "vue";

const HomeComponent = defineAsyncComponent(
  () => import("./components/HomeVue.vue")
);
</script>

<template>
  <HomeComponent />
</template>

<style>
html,
body {
  scrollbar-gutter: stable;
}
</style>
