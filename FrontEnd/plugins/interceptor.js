/*
 * @FileDescription: axios interceptor
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-28
*/
import qs from 'qs';

export default ({store, $cookies, $axios}) => {
  if (process.client) {
    $axios.defaults.withCredentials = true;
    $axios.defaults.baseURL = '/backend';

    $axios.onRequest(config => {
      config.xsrfCookieName = 'csrftoken';
      config.xsrfHeaderName = 'X-CSRFToken';
      config.headers.common['Key'] = $cookies.get('key');

      if (Object.prototype.toString.call(config.data) !== '[object FormData]') {
        config.data = qs.stringify(config.data, {
          allowDots: true
        });
      }
      if (store.state.debug) {
        console.log('ajax config', config);
      }
      return config;
    })

    $axios.onResponse(response => {
        if (store.state.debug) {
          console.log('ajax response', response);
        }
        let key;
        if ('key' in response.headers) {
          key = response.headers['key'];
        } else {
          key = 'Visitor';
        }
        $cookies.set('ajax-ready', true);
        $cookies.set('key', key);
        store.commit('set_admin', key !== 'Visitor');
      }
    )

    $axios.onError(error => {
      if (store.state.debug) {
        console.log('ajax error', error);
      }
      $cookies.set('ajax-ready', store.state.debug);
      $cookies.set('key', store.state.debug ? 'Admin' : 'Visitor');
      store.commit('set_admin', store.state.debug);
    })

    if (!$cookies.get('ajax-ready')) {
      $axios.get('/csrf');
    } else {
      store.commit('set_admin', $cookies.get('key') !== 'Visitor');
    }
  }
}
