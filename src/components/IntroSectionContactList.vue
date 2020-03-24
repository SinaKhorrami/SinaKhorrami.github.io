<template>
  <div class="row">
    <IntroSectionContactListItem
      v-for="media in medias"
      :key="media.id"
      :href="media.link"
      :size="iconSize"
      :src="media.iconSrc"
      :background-color="media.backgroundColor"
    />
  </div>
</template>

<script>
import Resume from '@/assets/resume.pdf'
import GmailIcon from '@/assets/gmail.svg'
import LinkedinIcon from '@/assets/linkedin.svg'
import KaggleIcon from '@/assets/kaggle.svg'
import AdobeAcrobatReaderIcon from '@/assets/adobeacrobatreader.svg'

import IntroSectionContactListItem from './IntroSectionContactListItem'

export default {
  name: 'IntroSectionContactList',
  computed: {
    iconSize: () => 24,
    medias: () => [
      {
        id: 'gmail',
        iconSrc: GmailIcon,
        backgroundColor: '#D14836',
        link: 'mailto:sinakhorami94@gmail.com'
      },
      {
        id: 'linkedin',
        iconSrc: LinkedinIcon,
        backgroundColor: '#FFFFFF',
        link: 'https://www.linkedin.com/in/sina-khorami/'
      },
      {
        id: 'kaggle',
        iconSrc: KaggleIcon,
        backgroundColor: '#20BEFF',
        link: 'https://kaggle.com/sinakhorami/'
      },
      {
        id: 'resume',
        iconSrc: AdobeAcrobatReaderIcon,
        backgroundColor: '#EE3F24',
        link: Resume
      }
    ]
  },
  components: {
    IntroSectionContactListItem
  }
}
</script>
