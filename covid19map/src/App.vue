<template>
  <div id="app">
    <Germanymap/>
    <dailyConfirm/>
  </div>
</template>

<script>
import Germanymap from './components/GermanyMap'
import dailyConfirm from './components/dailyConfirm'

export default {
  name: 'App',
  components: {
   Germanymap,
   dailyConfirm
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
