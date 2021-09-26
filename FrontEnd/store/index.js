export const state= () => ({
  backend:{
      //后端域名和端口，前端域名和端口在package.json中修改
      domain:"localhost",
      port:"8000",
  },
  authority:{
        key: "Visitor",
        is_admin: false,
  },
});

export const mutations = {
    set_admin(state, is_admin) {
      state.authority.is_admin = is_admin;
    },
    set_key(state, key){
      state.authority.key = key;
    }
};
