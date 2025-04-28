// word class
// describe = description
// abcdefjhijklmnopqrstuvwxyz
export const partOfSpeech = {
  adj: {
    full: "adjective",
    satisfies: "形容词",
    describe: "表示人或事物的特征"
  },
  adv: {
    full: "adverb",
    satisfies: "副词",
    describe: ""
  },
  art: {
    full: "article",
    satisfies: "冠词",
    describe: ""
  },
  conj: {
    full: "conjunction",
    satisfies: "连词",
    describe: ""
  },
  interj: {
    full: "interjection",
    satisfies: "感叹词",
    describe: ""
  },
  num: {
    full: "numeral",
    satisfies: "数词",
    describe: ""
  },
  n: {
    full: "noun",
    satisfies: "名词",
    describe: ""
  },
  prep: {
    full: "preposition",
    satisfies: "介词",
    describe: ""
  },
  pron: {
    full: "pronoun",
    satisfies: "代词",
    describe: ""
  },
  v: {
    full: "verb",
    satisfies: "动词",
    describe: ""
  },
  // Special
  vt: {
    full: "verb",
    satisfies: "及物动词",
    describe: ""
  },
  vi: {
    full: "verb",
    satisfies: "不及物动词",
    describe: ""
  }
}

export type PartOfSpeech = keyof typeof partOfSpeech
