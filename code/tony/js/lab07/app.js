const App = {
    el: '#app',
    data () { return { testData: '', emoji: '', debug: '' } },
    async mounted() {
        document.getElementById('entry').focus()
        this.emoji = await getEmojiData()
        this.debug += `<pre>${JSON.stringify(this.emoji,null,2)}</pre>`
    },
    methods: {
        typeAhead(ev) {
            // this.debug += `<pre>${ev.target.value}</pre>`
            // this.debug = this.emoji.filter((v,i,a)=>v.keywords.find((v,i,a)=>v.match(ev.target.value))).map(e=>e.character).join('')
            // this.debug = this.emoji.filter((v,i,a)=>v.keywords.find((v,i,a)=>v.match(ev.target.value))).map(e=>[e.character,e.name].join('')).join('<br>')
            this.debug = this.emoji.filter((v,i,a)=>v.keywords.find((v,i,a)=>v.match(ev.target.value))).map(e=>e.character).join('')
        }
    }
}

const app = Vue.createApp(App)
app.mount('#app')

async function getTestData() {
    const testData = localStorage.getItem('emojiTestData')
    const endpoint = 'https://raw.githubusercontent.com/webavant/data/main/emoji-test.txt'
    testData || localStorage.setItem('emojiTestData', await axios.get(endpoint).then(res => res.data))
    return localStorage.getItem('emojiTestData')
}

async function getEmojiData() {
    const data = await getTestData()
    const emoji = []

    data.split(/^# group: /mg).forEach((g, i) => {
        if (i < 1) { return }

        const group = g.match(/^.*$/m)[0]
        g.split(/^# subgroup: /mg).forEach((sg, ii) => {
            if (ii < 1) { return }

            const subgroup = sg.match(/^.*$/m)[0]
            sg.split(/^/mg).forEach((em, iii) => {
                if (iii < 1 || em.match(/^(#|\n)/mg) || !em.match(/; fully-qualified/)) { return }
                let splits = em.split(/;|#\s+\S+\s+E/)

                const codepoints = splits[0].trim().split(' ').map(e=>Number(`0x${e}`))
                const character = codepoints
                    .map(e => String.fromCodePoint(e)).join('')
                const version = Number(splits[2].split(/\s+/,1)[0])
                splits = splits[2].split(/\d+\.\d+\s+|:\s+/).map(e=>e.trim())
                const name = splits[1]
                const keywords = name.split(' ').concat(group.split(' ')).concat(subgroup.split(' '))
                const item = {name:name,keywords,keywords,group:group,subgroup:subgroup,codepoints:codepoints,character:character,version:version}
                if (splits[2]) { item.modifiers = splits[2].split(',').map(e => e.trim()) }
                emoji.push(item)
            })
        })
    })
    return emoji
}