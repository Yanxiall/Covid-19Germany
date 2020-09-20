<template>
  <div class="main">
    <CovidTable/>
    <Germanymap/>
    <dailyConfirm/>
    <h2 class="title">
        statistics
      </h2>
      <div class="statistics">
        <div>
          <div class="number">{{total.confirmed}}</div>
          <div class="desc">Confirmed </div>
        </div>
        <div>
          <div class="number">{{total.cured}}</div>
          <div class="desc">Cured</div>
        </div>
        <div>
          <div class="number">{{total.death}}</div>
          <div class="desc">Death</div>
        </div>
        <div>
          <div class="number">{{total.newdeath}}</div>
          <div class="desc">New Death</div>
        </div>
         <div>
          <div class="number">{{total.newconfirm}}</div>
          <div class="desc">New Confirmed</div>
        </div>
      </div>
      <div class="statinfo">

      </div>    
  </div>
</template>

<script>
import Germanymap from './components/GermanyMap'
import dailyConfirm from './components/dailyConfirm'
import todaydata from './assets/today.json'
import CovidTable from './components/CovidTable'
export default {
  name: 'App',
  components: {
   Germanymap,
   dailyConfirm,
   CovidTable
  },
  data(){
     return {
       total:''
     }
  },
  mounted(){
    this.total = todaydata.germantotal
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.main {
  width: 80%;
  margin: 10px auto;
}

.main .title {
  text-decoration: #22aeb4;
}
.main .title ::before {
  content: '';
  width: 20px;
  height: 100%;
  background-color: #22aeb4;
}

.main .title .updateTime {
  font-size: 14px;
  font-weight: 500;
  float: right;
}

.main .statistics {
  display: flex;
  justify-content: space-between;
  text-align: center;
  background-color: #f5f6f7;
  padding: 20px 40px;
  border-radius: 10px;
}

.main .number {
  color: #22aeb4;
  font-size: 20px;
  font-weight: 900;
}
</style>
