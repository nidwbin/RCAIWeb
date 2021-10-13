export const state = () => ({
  admin: false,
  debug: true,
});

export const mutations = {
  set_admin(state, admin) {
    state.admin = state.debug ? true : admin;
  }
};
