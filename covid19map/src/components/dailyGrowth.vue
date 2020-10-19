<template>
  <div>
    <highcharts :options="chartOptions" :callback="myCallback"></highcharts>
  </div>
</template>

<script>
import growth from '../assets/growth.json'
export default {
  data() {
    return {
      chartOptions: {
        title: {
          text: "Daily New Cases",
          style: {
            fontWeight: 'bold',
            fontSize: '1.6vw'
          }
        },
        xAxis: {
          type: 'datetime',
			    dateTimeLabelFormats: {
				     day: '%e of %b'
			}
      	},
        yAxis:[ {
          opposite: true,
          title: {
            id:0,
            text: "infected cases per day"
          }
        },
        {
          title: {
            id:1,
            text: "death cases per day"
          }
        }
        ],
        legend: {
          layout: "vertical",
          align: "right",
          verticalAlign: "middle"
        },
        plotOptions: {
          series: {
            label: {
              connectorAllowed: false
            },
            pointStart: Date.UTC(2020, 1, 25),
			      pointInterval: 24 * 3600 * 1000 // one day
          }
        },
        series: [
          {
            name: "infected cases per day",
            yAxis: 0,
            data: growth["DayInfected"]
          },
          {
            name: "dead cases per day",
            yAxis: 1,
            color:'#49ff2f',
            data: growth["DayDeath"]
          }
        ],
        responsive: {
          rules: [
            {
              condition: {
                maxWidth: 500
              },
              chartOptions: {
                legend: {
                  layout: "horizontal",
                  align: "center",
                  verticalAlign: "bottom"
                }
              }
            }
          ]
        }
      }
    };
  },
  methods: {
    myCallback() {
      console.log("this is callback function");
    }
  }
};
</script>

<style>
.highcharts-container {
  width: 80vw;
  height: 53.333vw;
  border: 0.133vw solid #ddd;
  margin: auto;
}
</style>