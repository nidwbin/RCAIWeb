export const state = () => ({
  admin: false,
  debug: false,
  image_base: '/media/images/',
});

export const mutations = {
  set_admin(state, admin) {
    state.admin = state.debug ? true : admin;
  }
};
