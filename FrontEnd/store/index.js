export const state= () => ({
    domain:"http://localhost",
    port:"4980",
    location:"/",
    is_admin: false,
});

export const mutations = {
    change_admin(state, is_admin) {
      state.is_admin = is_admin;
    },
    change_location(state, location){
      state.location=location;
    }
};
