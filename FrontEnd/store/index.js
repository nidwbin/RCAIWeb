export const state= () => ({
  backend:{
      //后端域名和端口，前端域名和端口在package.json中修改
      domain:"http://localhost",
      port:"8000",
  },
  com_sync:{
    location: "/",
    message: "",
  },
  authority:{
        is_admin: false,
  },
});

export const mutations = {
    set_admin(state, is_admin) {
      state.authority.is_admin = is_admin;
    },
    set_location(state, location){
      state.com_sync.location=location;
    },
    set_message(state, message){
      state.com_sync.message = message;
    },
};
