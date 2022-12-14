<script setup lang="ts">

</script>

<template>
  <main class="bg-sky-100 dark:bg-slate-900 text-sky-700 dark:text-sky-300 min-h-screen z-[-1000]">
    <router-view />
  </main>
</template>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Be Vietnam Pro', 'Plus Jakarta Sans', 'Poppins', 'Ubuntu', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}

:root {
  /* clamp */
  --card-title: clamp(.925rem, 2.75vw, 1.2rem);
  --card-detail: clamp(.665rem, 2.5vw, .85rem);
  --smallest-icon: clamp(.6rem, 1.75vw, .75rem);
  --smaller-icon: clamp(.7rem, 2vw, .95rem);
  --icon: clamp(.7rem, 2.15vw, 1rem);
  --larger-icon: clamp(.8rem, 2.3vw, 1.2rem);
  --largest-icon: clamp(.9rem, 2.5vw, 1.35rem);
  --letter-space: clamp(.1rem, .5vw, .3rem);
  --title: clamp(1.1rem, 2.25vw, 1.6rem);
  --big-title: clamp(1.5rem, 3.25vw, 3rem);
  --small-title: clamp(.475rem, 2.35vw, 1rem);
  --sub-title: clamp(1.1rem, 3vw, 1.35rem);
  --mini-icon: clamp(.6rem, 1.95vw, .8rem);
  --logo: clamp(.735rem, 2.15vw, 1.05rem);
  --footer-cap: clamp(.55rem, 1.5vw, .65rem);
  --subtitle: clamp(1rem, 4vw, 1.75rem);
  --landing-foot: clamp(.625rem, 1.65vw, 1rem);

  --sidebar-width: 40vw;
  --sidebar-minwidth: 280px;
  --sidebar-maxwidth: 21rem;

  --trans: #7dd4fc2c;
}

::-webkit-scrollbar {
  width: 5px;
  height: 5px;
}

::-webkit-scrollbar-track {
  background-color: #f8fafc;
  border-radius: 5px 5px 0 0;
  margin: 0 .75rem;
}

::-webkit-scrollbar-thumb {
  background-color: #38bdf8;
  border-radius: 5px 5px 0 0;
  cursor: pointer;
}

::-webkit-scrollbar-thumb:hover {
  background-color: #0ea5e9;
}

.ellips {
  overflow: hidden;
  text-overflow: ellipsis;
  -webkit-box-orient: vertical;
  display: block;
  display: -webkit-box;
}

.cards {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(20rem, 1fr));
}

@media all and (max-width: 300px) {
  .cards {
    grid-template-columns: repeat(auto-fit, minmax(12rem, 1fr));
  }
}

.grids {
  grid-template-columns: repeat(auto-fit, minmax(11rem, 1fr));
}

h1 {
  font-size: xx-large !important;
}

h2 {
  font-size: x-large !important;
}

h3 {
  font-size: large !important;
}

h4 {
  font-size: small !important;
}

h5 {
  font-size: x-small !important;
}

h6 {
  font-size: xx-small !important;
}
</style>
