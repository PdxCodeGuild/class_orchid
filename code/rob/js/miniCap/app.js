import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'
import { DEV_ID, AUTH_KEY } from './hide.js'

createApp({
    data() {
        return {
          message: 'Smite!',
          ses_id: {},
          role: 'All',
          gods: [],
          filtergods: [],
          skins: [],
          godStats: {},
          name: '',
        }
      },
      components: {
        godcard: {
            props: {
                god: {},
            },
            template: `<div @click="$emit('selectgod', god)" class="godCard"><img :src="god.godIcon_URL"><h3>{{god.Name}}</h3><h4>{{god.Roles}}</h4></div>`,
        },
      },
      methods: {
        startSession(){
            var date = new Date();
            let fullUtcDate = date.getUTCFullYear() + ("0" + (date.getUTCMonth() + 1)).slice(-2) + ("0" + date.getUTCDate()).slice(-2) + ("0" + date.getUTCHours() ).slice(-2) + ("0" + date.getUTCMinutes()).slice(-2) + ("0" + date.getUTCSeconds()).slice(-2)
            let hashed = CryptoJS.MD5(`${DEV_ID}` + `createsession` + `${AUTH_KEY}` + `${fullUtcDate}`).toString();
            axios.get(`https://api.smitegame.com/smiteapi.svc/createsessionjson/${DEV_ID}/${hashed}/${fullUtcDate}`).then((response) => {
                // handle success
                console.log(response);
                this.ses_id = response.data
                localStorage.setItem('ses_id', JSON.stringify(this.ses_id))
            })
            .catch((error) => {
                // handle error
                console.log(error);
            })
            
        },
        testSession(){
            var date = new Date();
            let fullUtcDate = date.getUTCFullYear() + ("0" + (date.getUTCMonth() + 1)).slice(-2) + ("0" + date.getUTCDate()).slice(-2) + ("0" + date.getUTCHours() ).slice(-2) + ("0" + date.getUTCMinutes()).slice(-2) + ("0" + date.getUTCSeconds()).slice(-2)
            let hashed = CryptoJS.MD5(`${DEV_ID}` + `testsession` + `${AUTH_KEY}` + `${fullUtcDate}`).toString();
            
            this.ses_id = JSON.parse(localStorage.getItem('ses_id'))
            axios.get(`https://api.smitegame.com/smiteapi.svc/testsessionjson/${DEV_ID}/${hashed}/${this.ses_id.session_id}/${fullUtcDate}`).then((response) => {
                // handle success
                console.log(response);
                console.log(this.ses_id)
            })
            .catch((error) => {
                // handle error
                console.log(error);
            })
           
        },
        getGods(){
            var date = new Date();
            let fullUtcDate = date.getUTCFullYear() + ("0" + (date.getUTCMonth() + 1)).slice(-2) + ("0" + date.getUTCDate()).slice(-2) + ("0" + date.getUTCHours() ).slice(-2) + ("0" + date.getUTCMinutes()).slice(-2) + ("0" + date.getUTCSeconds()).slice(-2)
            let hashed = CryptoJS.MD5(`${DEV_ID}` + `getgods` + `${AUTH_KEY}` + `${fullUtcDate}`).toString();
            this.ses_id = JSON.parse(localStorage.getItem('ses_id'))
            axios.get(`https://api.smitegame.com/smiteapi.svc/getgodsjson/${DEV_ID}/${hashed}/${this.ses_id.session_id}/${fullUtcDate}/1`).then((response) => {
                // handle success
                console.log(response.data);
                this.gods = response.data
            })
            .catch((error) => {
                // handle error
                console.log(error);
            })

        },
        getSkins(){
            var date = new Date();
            let fullUtcDate = date.getUTCFullYear() + ("0" + (date.getUTCMonth() + 1)).slice(-2) + ("0" + date.getUTCDate()).slice(-2) + ("0" + date.getUTCHours() ).slice(-2) + ("0" + date.getUTCMinutes()).slice(-2) + ("0" + date.getUTCSeconds()).slice(-2)
            let hashed = CryptoJS.MD5(`${DEV_ID}` + `getgodskins` + `${AUTH_KEY}` + `${fullUtcDate}`).toString();
            this.gods.forEach(god => {
                axios.get(`https://api.smitegame.com/smiteapi.svc/getgodskinsjson/${DEV_ID}/${hashed}/${this.ses_id.session_id}/${fullUtcDate}/${god.id}/1`).then((response) => {
                // handle success
                console.log(response.data[0]);
                this.skins.push(response.data[0])
            })
            .catch((error) => {
                // handle error
                console.log(error);
            })
            })
        },
        onChange(event){
            this.role = event.target.value
        },
        getStats(g){
            this.godStats = {}
            this.godStats.Name = g.Name
            this.godStats.one = g.Ability1
            this.godStats.two = g.Ability2
            this.godStats.three = g.Ability3
            this.godStats.four = g.Ability4
            console.log(this.godStats)
            setTimeout(() => {
                this.godStats = {};
            }, 2000);
        }
      },
      computed: {
        nameChange(){
            if(this.name == ''){
                this.filtergods = []
            }
            this.gods.forEach((e) => {
                if(e.Name == this.name){
                    this.filtergods.push(e)
                }
            })
        }
      }
}).mount('#app')
