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
        <div class="confirmNum">{{ total.confirmed }}</div>
        <div class="desc">Total Cases</div>
      </div>
      <div>
        <div class="recoverNum">{{ total.cured }}</div>
        <div class="desc">Total Recovered</div>
      </div>
      <div>
        <div class="deathNum">{{ total.death }}</div>
        <div class="desc">Total Deaths</div>
      </div>
      <div>
        <div class="activeCases">{{ total.activeCases }}</div>
        <div class="desc">Active Cases</div>
      </div>
      <div>
        <div class="newdeathNum">{{ total.newdeath }}</div>
        <div class="desc">New Deaths</div>
      </div>
      <div>
        <div class="newconfirmNum">{{ total.newconfirm }}</div>
        <div class="desc">New Cases</div>
      </div>
    </div>
    <div class="subtitle">
      <h2>Case Numbers Map</h2>
      <Germanymap />
    </div>
    <div class="subtitle">
      <h2>Daily Total Cases</h2>
      <dailyConfirm />
    </div>
    <div class="subtitle">
      <h2>Cases per day</h2>
      <dailyGrowth />
    </div>
    <div class="subtitle">
      <h2>Case Numbers by State</h2>
      <CovidTable />
    </div>
  </div>
</template>

<script>
import Germanymap from "./components/GermanyMap";
import dailyConfirm from "./components/dailyConfirm";
import dailyGrowth from "./components/dailyGrowth";
import todaydata from "./assets/today.json";
import CovidTable from "./components/CovidTable";
export default {
  name: "App",
  components: {
    Germanymap,
    dailyConfirm,
    dailyGrowth,
    CovidTable,
  },
  data() {
    return {
      imgSrc: require("./assets/corona_banner.jpg"),
      total: "",
    };
  },
  mounted() {
    this.total = todaydata.germantotal;
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
.main {
  font-family: "Times New Roman", Times, serif;
  width: 80%;
  margin: 0vw auto 1.333vw auto;
}
.main .banner {
  font-size: 0;
}
.main .totalInfo {
  padding: 2.667vw 0vw 2.667vw 0vw;
  background-color: turquoise;
  padding-left: 1.333vw;
}
.totalInfo h2 {
  font-size: 2vw;
}
.main .statistics {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  text-align: center;
  background-color: #f5f6f7;
  padding: 2.667vw 5.333vw;
  border-radius: 1.333vw;
}
.main .subtitle h2 {
  padding-top: 2.667vw;
  padding-bottom: 2.667vw;
  padding-left: 1.333vw;
  background-color: turquoise;
  font-size: 2vw;
}
.main .activeCases {
  color: indigo;
  font-size: 2vw;
  font-weight: 1000;
}
.main .confirmNum {
  color: #22aeb4;
  font-size: 2vw;
  font-weight: 1000;
}
.main .recoverNum {
  color: green;
  font-size: 2vw;
  font-weight: 1000;
}
.main .deathNum {
  color: red;
  font-size: 2vw;
  font-weight: 1000;
}
.main .newdeathNum {
  color: crimson;
  font-size: 2vw;
  font-weight: 1000;
}
.main .newconfirmNum {
  color: mediumblue;
  font-size: 2vw;
  font-weight: 1000;
}
.main .desc {
  font-weight: 700;
  font-size: 1.4vw;
}
</style>
