<!--
 * @FileDescription: axios interceptor
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-28
 -->
import qs from 'qs';

export default({store, $cookies, $axios}) => {
  if(process.client) {
    $axios.defaults.withCredentials = true;
    $axios.defaults.baseURL = 'http://192.168.11.233:8001/backend';

    $axios.onRequest(config => {
      config.xsrfCookieName = 'csrftoken';
      config.xsrfHeaderName = 'X-CSRFToken';
      config.headers.common['Key'] = $cookies.get('key');
      config.data = qs.stringify(config.data, {
        allowDots:true
      });
      return config;
    })

    $axios.onResponse(response => {
      let key;
      if ('key' in response.headers) {
        key = response.headers['key'];
      } else {
        key = "Visitor";
      }
      $cookies.set("ajax-ready", true)
      $cookies.set("key", key)
      store.commit("set_admin", key===undefined ? false : key !== "Visitor");
    })

    $axios.onError(error => {
      console.log(error);
      $cookies.set("ajax-ready", false);
      store.commit("set_key", "Visitor");
      store.commit("set_admin", false);
    })
  }
}
