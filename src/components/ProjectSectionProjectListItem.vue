<template>
  <div class="col text-left">
    <b-card
      class="shadow my-3"
      body-class="d-flex flex-column card-250"
    >
      <b-card-title>
        {{ name }}
      </b-card-title>
      <b-card-sub-title
        class="border-top border-4 w-50 py-2 my-2"
        :style="{ borderColor: `${primaryLanguage.color} !important` }"
      >
        {{ primaryLanguage.name }}
      </b-card-sub-title>
      <b-card-text>
        {{ description }}
      </b-card-text>
      <b-link
        class="stretched-link"
        rel="noopener noreferrer"
        target="_blank"
        :href="url"
      />
      <b-card-text class="small text-muted mt-auto">
        Created about {{ createdAtRelative }} ago
      </b-card-text>
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'ProjectSectionProjectListItem',
  props: {
    name: String,
    createdAt: String,
    description: String,
    url: String,
    primaryLanguage: Object
  },
  computed: {
    createdAtRelative: function () {
      const date = new Date(this.createdAt)

      return this.ago(date)
    }
  },
  methods: {
    ago: (val) => {
      val = 0 | (Date.now() - val) / 1000
      let unit
      const length = { second: 60, minute: 60, hour: 24, day: 7, week: 4.35, month: 12, year: 10000 }
      let result

      for (unit in length) {
        result = val % length[unit]
        if (!(val = 0 | val / length[unit])) {
          return result + ' ' + (result - 1 ? unit + 's' : unit)
        }
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.border-4 {
  border-width: 4px !important;
}
.card-250 {
  min-height: 250px;
}
</style>
