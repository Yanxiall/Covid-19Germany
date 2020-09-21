<template>
  <div class="mapdata">
    <highcharts :constructorType="'mapChart'" class="hc" :options="chartOptions" ref="chart"></highcharts>
  </div>
</template>

<script>
import GermMap from '@highcharts/map-collection/countries/de/de-all.geo.json'
import data from '../assets/today.json'
var convertData = function (data) {
        var res = []
        //states info
        var states = data["children"]
        for (var i = 0; i < states.length; i++) {
            res.push({
              name: states[i].name,
              value: states[i].confirm
            })
        }
        return res
}
export default {
  data() {
    return {
      chartOptions: {
        chart: {
          map: GermMap
        },
        title: {
          text: 'Covid-19 Map with Case Numbers'
        },
        mapNavigation: {
          enabled: true,
          buttonOptions: {
            alignTo: 'spacingBox'
          }
        },
        colorAxis: {
          min: 0
        },
        series: [{
          name: 'confirmed data',
          states: {
            hover: {
              color: '#BADA55'
            }
          },
          dataLabels: {
            enabled: true,
            format: '{point.name}'
          },
          allAreas: true,
          joinBy: 'name',
          data: convertData(data)
               
        }]
      }
    };
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
