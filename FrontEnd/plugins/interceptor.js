export default({store, $cookies, $axios}) => {

    $axios.onRequest(config => {
      config.xsrfCookieName = 'csrftoken';
      config.xsrfHeaderName = 'X-CSRFToken';
      config.headers.common['Content-Type'] = 'application/json';
      config.headers.common['X-CSRFToken'] = $cookies.get("csrf");
      config.headers.common['Key'] = store.state.authority.key;
      return config
    })

    $axios.onResponse(response => {
      let key = response.headers.common['Key'];
      $cookies.set("ajax-ready", true)
      store.commit("set_key", key);
      store.commit("set_admin",key!=="Visitor");
    })

    $axios.onError(error => {
        console.log(error);
        $cookies.set("ajax-ready",false);
        store.commit("set_key", "Visitor");
        store.commit("set_admin",true);
    })

}
