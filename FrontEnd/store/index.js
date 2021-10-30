export const state = () => ({
  admin: false,
  debug: false,
  image_base: 'http://localhost:8000/media/images/',
});

export const mutations = {
  set_admin(state, admin) {
    state.admin = state.debug ? true : admin;
  }
};
