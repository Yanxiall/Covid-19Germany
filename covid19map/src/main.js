// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Highcharts from 'highcharts'
import Maps from 'highcharts/modules/map';
import HighchartsVue from 'highcharts-vue';

Vue.config.productionTip = false

Maps(Highcharts);
Vue.use(HighchartsVue);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})
