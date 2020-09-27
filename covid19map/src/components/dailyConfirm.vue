<template>
  <div>
    <highcharts :options="chartOptions" :callback="myCallback"></highcharts>
  </div>
</template>

<script>
import daily from '../assets/daily.json'
export default {
  data() {
    return {
      chartOptions: {
        title: {
          text: "Daily Cases",
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
        yAxis: {
          title: {
            text: "total coronavirus cases"
          }
        },
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
            pointStart: Date.UTC(2020, 2, 12),
			      pointInterval: 24 * 3600 * 1000 // one day
          }
        },
        series: [
          {
            name: "confirmed",
            data: daily["confirmed"]
          },
          {
            name: "recovered",
            data: daily["cured"]
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