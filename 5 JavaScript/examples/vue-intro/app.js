const App = {
    el: '#app',
    data: () => {
        return {
            className: 'Class Orchid',
            startDate: 'July 11, 2022',
            repo: 'https://github.com/PdxCodeGuild/class_orchid',
            repoTag: '<a href="https://github.com/PdxCodeGuild/class_orchid">Github repository</a>',
            kudos: 0,
            inputField: 'starter data',
            inputField2: '',
            a: 0,
            b: 0,
            bSeasonTotal: 89,
            boxRed: false,
            transparent: false,
            students: [
                'Cesar',
                'Faith',
                'Jen',
                'Jordyn',
                'Mileidy',
                'Pat',
                'Rob',
                'Teyon',
                'Tony',
                'Vel',
            ],
            staff: [
                {
                    name: 'Danny',
                    title: 'instructor',
                    active: true
                },
                {
                    name: 'Gage',
                    title: 'TA',
                    active: true
                },
                {
                    name: 'Matt',
                    title: 'TA',
                    active: false
                },
                {
                    name: 'Mitch',
                    title: 'TA',
                    active: false
                },
                {
                    name: 'Pete',
                    title: 'instructor',
                    active: false
                },

            ],
            seasons: {
                spring: ['March', 'April', 'May'],
                summer: ['June', 'July', 'August'],
                fall: ['September', 'October', 'November'],
                winter: ['December', 'January', 'February']
            },
        }
    },
    methods: {
        getGradDate() {
            let result = new Date(this.startDate);
            result.setDate(result.getDate() + 102);
            return result.toDateString()
        },
        giveKudos(num) {
            this.kudos += num
        },
        logInput(e) {
            this.inputField = e.target.value
        }

    },
    computed: {
        scoreA() {
            return this.a + 32
        },
        scoreB() {
            return this.b + this.bSeasonTotal
        },
        boxClasses() {
            return {
                red: this.boxRed,
                transparent: this.transparent
            }
        },
        activeStaff() {
            return this.staff.filter(s => s.active)
        }
    }
}

const app = Vue.createApp(App)
app.mount('#app')