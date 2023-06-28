<script setup lang="ts">
import { onMounted } from "@vue/runtime-core";
import Local from '@/api/local';

onMounted(() => {
  Local.setLocalData('theme', true);
})
</script>

<template>
  <div class="max-w-screen min-h-screen overflow-hidden">
    <router-view />
  </div>
</template>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Be Vietnam Pro', cursive, 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

::-webkit-scrollbar {
  width: 5px;
  height: 5px;
}

::-webkit-scrollbar-track {
  background-color: transparent;
}

::-webkit-scrollbar-thumb {
  background-color: #0284c7;
}

::-webkit-scrollbar-thumb:hover {
  background-color: #0369a1;
}

.left-0 img {
  animation: cloud calc(10s * var(--i)) linear infinite;
}

.inv img {
  filter: brightness(0) saturate(100%) invert(66%) sepia(34%) saturate(6212%) hue-rotate(193deg) brightness(108%) contrast(96%)
}

@keyframes cloud {
  0% {
    transform: translateX(-100%);
  }

  100% {
    transform: translateX(100%);
  }
}
</style>