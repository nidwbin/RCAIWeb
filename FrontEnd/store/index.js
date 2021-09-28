export const state = () => ({
  admin: false,
});

export const mutations = {
  set_admin(state, admin) {
    state.admin = admin;
  }
};
