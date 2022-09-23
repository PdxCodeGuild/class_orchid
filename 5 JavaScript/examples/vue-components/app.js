Vue.component('counter', {
    template: '<button @click="count++">{{ count }}</button>',
    data: () => {
        return {
            count: 0
        }
    }
})

Vue.component('BookItem', {
    template: `
        <p class="book" v-on="checkedOut ? {click: checkIn} : {click: checkOut}" :class="{out: checkedOut}">
            <strong>{{ title }}</strong><br>
            {{ author }}<br>
            checked out {{ timesCheckedOut }} times
        </p>`,
    data: () => {
        return {
            checkInDate: Date.now(),
            checkOutDate: null,
            timesCheckedOut: 0
        }
    },
    props: {
        title: {
            type: String,
            required: true,
            validator: (t) => {
                // return any boolean
                return t.length > 6
            }
        },
        author: String
    },
    methods: {
        checkOut() {
            this.checkOutDate = Date.now()
            this.timesCheckedOut++
        },
        checkIn() {
            this.checkInDate = Date.now()
        }
    },
    computed: {
        checkedOut() {
            return this.checkOutDate > this.checkInDate
        }
    }
})


new Vue({
    el: '#app',
    data: {
        libraryName: 'Class Orchid Library',
        books: [
            {
                title: "The Farming of Bones",
                author: "Edwidge Danticat"
            },
            {
                title: "Future Home of the Living God",
                author: "Louise Erdritch"
            },
            {
                title: "Last Night at the Telegraph Club",
                author: "Malinda Lo"
            },
            {
                title: "Braiding Sweetgrass",
                author: "Robin Wall Kimmerer"
            },
            {
                title: "The Bluest Eye",
                author: "Toni Morrison"
            },
            {
                title: "A Long Petal of the Sea",
                author: "Isabel Allende",
            },
            {
                title: "A Tale for the Time Being",
                author: "Ruth Ozeki"
            },
            {
                title: "Disorientation",
                author: "Elaine Hsieh Chou"
            },
            {
                title: "The Fifth Season",
                author: "N. K. Jemisin"
            },
            {
                title: "Americanah",
                author: "Chimamanda Ngozi Adichie"
            },
            {
                title: "Woman at Point Zero",
                author: "Nawal El-Saadawi"
            },
            {
                title: "Persepolis",
                author: "Marjane Satrapi"
            },
            {
                title: "In the Dream House",
                author: "Carmen Maria Machado"
            },
            {
                title: "Gold Diggers",
                author: "Sanjeetha Sathian"
            },
            {
                title: "Kindred",
                author: "Octavia Butler"
            },
            {
                title: "Akata Witch",
                author: "Nnedi Okorafor"
            },
            {
                title: "Passing",
                author: "Nella Larsen"
            },
            {
                title: "Black Water Sister",
                author: "Zen Cho"
            },
            {
                title: "Their Eyes Were Watching God",
                author: "Zora Neal Hurston"
            },
            {
                title: "Iron Widow",
                author: "Xiran Jay Zhao"
            },
            {
                title: "Jasmine",
                author: "Bharati Mukherjee"
            },
        ]
    }
})
