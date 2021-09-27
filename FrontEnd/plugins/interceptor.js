import qs from 'qs';

export default({store, $cookies, $axios}) => {
  if(process.client) {
    $axios.defaults.withCredentials = true;

    $axios.onRequest(config => {
      config.xsrfCookieName = 'csrftoken';
      config.xsrfHeaderName = 'X-CSRFToken';
      config.headers.common['Key'] = store.state.authority.key;
      config.data = qs.stringify(config.data, {
        allowDots:true
      });
      console.log(config);
      return config;
    })

    $axios.onResponse(response => {
      let key;
      if ('Key' in response.headers) {
        key = response.headers['Key'];
      } else {
        key = "Visitor";
      }
      $cookies.set("ajax-ready", true)
      store.commit("set_key", key);
      store.commit("set_admin", key !== "Visitor");
    })

    $axios.onError(error => {
      console.log(error);
      $cookies.set("ajax-ready", false);
      store.commit("set_key", "Visitor");
      store.commit("set_admin", false);
    })
  }
}
