<template>
  <div>
    <h3> Sina Khorrami </h3>
    <p class="text-monospace"> Developer </p>
    <a
      v-for="media in medias"
      :key="media.id"
      :href="media.link"
      target="_blank"
      rel="noopener noreferrer"
      class="mx-1"
    >
      <img
        :src="media.source"
        :alt="media.id"
        width="24"
      >
    </a>
  </div>
</template>

<script>
import Resume from '@/assets/resume.pdf'
import Gmail from '@/assets/gmail.svg'
import Linkedin from '@/assets/linkedin.svg'
import Kaggle from '@/assets/kaggle.svg'
import Github from '@/assets/github.svg'
import Stackoverflow from '@/assets/stackoverflow.svg'
import Cv from '@/assets/cv.svg'

export default {
  name: 'ContactInfo',
  computed: {
    medias: () => [
      {
        id: 'gmail',
        source: Gmail,
        link: 'mailto:sinakhorrami94@gmail.com'
      },
      {
        id: 'linkedin',
        source: Linkedin,
        link: 'https://www.linkedin.com/in/sina-khorrami/'
      },
      {
        id: 'kaggle',
        source: Kaggle,
        link: 'https://kaggle.com/sinakhorami/'
      },
      {
        id: 'github',
        source: Github,
        link: 'https://github.com/SinaKhorrami'
      },
      {
        id: 'stackoverflow',
        source: Stackoverflow,
        link: 'https://stackoverflow.com/users/9977321/'
      },
      {
        id: 'cv',
        source: Cv,
        link: Resume
      }
    ]
  }
}
</script>
