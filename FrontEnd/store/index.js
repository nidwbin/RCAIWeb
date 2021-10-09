export const state = () => ({
  admin: true,
  debug: true,
});

export const mutations = {
  set_admin(state, admin) {
    state.admin = admin;
  }
};
