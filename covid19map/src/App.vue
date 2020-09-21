<template>
  <div class="main">
      <div class="banner">   
        <img :src="imgSrc" width="100%" height="100%" alt="" />
      </div>
      <div class="totalInfo">
        <h2>Overview in Germany</h2>
      </div>
      <div class="statistics">
        <div>
          <div class="confirmNum">{{total.confirmed}}</div>
          <div class="desc">Total Cases</div>
        </div>
        <div>
          <div class="recoverNum">{{total.cured}}</div>
          <div class="desc">Total Recovered</div>
        </div>
        <div>
          <div class="deathNum">{{total.death}}</div>
          <div class="desc">Total Deaths</div>
        </div>
        <div>
          <div class="newdeathNum">{{total.newdeath}}</div>
          <div class="desc">New Deaths</div>
        </div>
         <div>
          <div class="newconfirmNum">{{total.newconfirm}}</div>
          <div class="desc">New Cases</div>
        </div>
      </div>
      <div class="subtitle">
         <h2>Case Numbers Map</h2>
         <Germanymap/>
      </div>
      <div class="subtitle">
         <h2>Daily Total Cases</h2>
         <dailyConfirm/>
      </div>
      <div class="subtitle">
        <h2>Case Numbers by State</h2>
        <CovidTable/>
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
       imgSrc:require('./assets/corona_banner.jpg'),
       total:''
     }
  },
  mounted(){
    this.total = todaydata.germantotal
  }
}
</script>

<style>
*{
  margin:0;
  padding:0;
}
.main {
  font-family: "Times New Roman", Times, serif;
  width: 80%;
  margin: 0px auto 10px auto;
}
.main .banner{
  font-size:0;
}
.main .totalInfo{
  padding:20px 0px 20px 0px; 
  background-color:turquoise;
  padding-left:10px;
}
.main .statistics {
  display: flex;
  justify-content: space-between;
  text-align: center;
  background-color: #f5f6f7;
  padding: 20px 40px;
  border-radius: 10px;
}
.main .subtitle h2{
  padding-top:20px;
  padding-bottom: 20px;
  padding-left:10px;
  background-color:turquoise;
}
.main .confirmNum {
  color: #22aeb4;
  font-size: 20px;
  font-weight: 1000;
}
.main .recoverNum {
  color:green;
  font-size: 20px;
  font-weight: 1000;
}
.main .deathNum {
  color:red;
  font-size: 20px;
  font-weight: 1000;
}
.main .newdeathNum {
  color:red;
  font-size: 20px;
  font-weight: 1000;
}
.main .newconfirmNum {
  color:orchid;
  font-size: 20px;
  font-weight: 1000;
}
.main .desc{
  font-weight: 700;
}
</style>
