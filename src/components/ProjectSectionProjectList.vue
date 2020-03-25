<template>
  <div class="row row-cols-3">
    <ProjectSectionProjectListItem
      v-for="(project, index) in projectList"
      v-bind:key="index"
      v-bind="project"
    />
  </div>
</template>

<script>
import Projects from '../../_data/projects.json'

import ProjectSectionProjectListItem from './ProjectSectionProjectListItem'

export default {
  name: 'ProjectSectionProjectList',
  computed: {
    projectList: () => Projects
  },
  components: {
    ProjectSectionProjectListItem
  }
}
</script>
