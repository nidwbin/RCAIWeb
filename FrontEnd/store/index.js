export const state = () => ({
  admin: false,
  debug: false,
});

export const mutations = {
  set_admin(state, admin) {
    state.admin = admin;
  }
};
