<template>
  <b-link
    rel="noopener noreferrer"
    target="_blank"
    :href="href"
  >
    <b-img
      class="m-1 rounded shadow"
      :width="size"
      :src="src"
      :style="{ backgroundColor }"
    />
  </b-link>
</template>

<script>
export default {
  name: 'IntroSectionContactListItem',
  props: {
    href: {
      type: String
    },
    size: {
      type: Number
    },
    src: {
      type: String
    },
    backgroundColor: {
      type: String
    }
  }
}
</script>
