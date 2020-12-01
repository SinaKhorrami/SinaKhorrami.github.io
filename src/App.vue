<template>
  <img
    class="rounded-circle shadow-sm"
    alt="Avatar"
    src="@/assets/avatar.jpg"
    width="200"
  >
  <ContactInfo class="mt-3" />
</template>

<script>
import ContactInfo from '@/components/ContactInfo'

export default {
  name: 'App',
  components: {
    ContactInfo
  }
}
</script>

<style lang="scss">
body {
  background-color: #f3f3f3 !important;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
