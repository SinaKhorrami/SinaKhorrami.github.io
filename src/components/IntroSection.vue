<template>
  <b-container
    id="IntroSection"
    class="d-flex flex-column justify-content-center align-items-center"
  >
    <b-img
      class="shadow"
      rounded="circle"
      src="@/assets/avatar.jpg"
      width="196px"
    />
    <h2 class="mt-3">
      {{ fullname }}
    </h2>
    <IntroSectionContactList />
  </b-container>
</template>

<script>
import IntroSectionContactList from './IntroSectionContactList'

export default {
  name: 'IntroSection',
  computed: {
    fullname: () => 'Sina Khorami'
  },
  components: {
    IntroSectionContactList
  }
}
</script>
