// arch = archaic = 过时词

import type { PartOfSpeech } from "./mod/class"

interface Relative {
  /* 词根 */
  root?: string
  /* 复数 */
  plural?: string
  /* 单数 */
  singular?: string
  /* 第三人称单数 - third person singular */
  tps?: string
  /* 第三人称复数 - third person plural */
  tpp?: string
  /* 过去式 - Past tense */
  past?: string
  /* 过去分词 - Past participle */
  pastParticiple?: string
  /* 现在式 - Present tense */
  present?: string
  /* 现在分词 - Present participle */
  presentParticiple?: string
  /* 将来式 - Future tense */
  future?: string
  /* 近义词 - synonym */
  synonym?: string
  /* 反义词 - antonym */
  antonym?: string
}

type Translate = {
  [key in PartOfSpeech]?: string[]
}

interface Vocabulary {
  /* 释义 */
  interpret: string
  /* 例句 */
  example: string
  /* 翻译 */
  translate: Translate
  /* 词义 */
  relative: Relative
  /* 易混淆词汇 - Confusing words */
  confuse: string[]
}

const ZH_CN: Record<string, Vocabulary> = {
  "vocabulary": {
    interpret: "释义",
    example: "",
    translate: {
      v: ["解释", "口译", "诠释", "说明", "把…理解为", "演绎", "领会"]
    },
    relative: {
      plural: "",
      singular: "",
      tps: ""
    },
    confuse: []
  }
}

const EN_US: Record<string, Vocabulary> = {}

export const vocabulary = {
  zh_CN: ZH_CN,
  en_US: EN_US
}
