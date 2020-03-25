<template>
  <b-container
    id="ProjectSection"
    class="my-5"
  >
    <ProjectSectionProjectList />
  </b-container>
</template>

<script>
import ProjectSectionProjectList from './ProjectSectionProjectList'

export default {
  name: 'ProjectSection',
  components: {
    ProjectSectionProjectList
  }
}
</script>
