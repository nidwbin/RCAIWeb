export default({store, $cookies, $axios}) => {
    $axios.defaults.withCredentials = true;

    $axios.onRequest(config => {
      if(process.client) {
        config.xsrfCookieName = 'csrftoken';
        config.xsrfHeaderName = 'X-CSRFToken';
        config.headers.common['Key'] = store.state.authority.key;
        return config;
      }
     })

     $axios.onResponse(response => {
       if(process.client) {
         let key;
         if ('Key' in response.headers) {
           key = response.headers['Key'];
         } else {
           key = "Visitor";
         }
         $cookies.set("ajax-ready", true)
         store.commit("set_key", key);
         store.commit("set_admin", key !== "Visitor");
       }
     })

     $axios.onError(error => {
       if(process.client) {
         console.log(error);
         $cookies.set("ajax-ready", false);
         store.commit("set_key", "Visitor");
         store.commit("set_admin", true);
       }
     })

}
