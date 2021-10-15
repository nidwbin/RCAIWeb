FROM node:latest

ENV NODE_ENV=production
ENV HOST=0.0.0.0

RUN mkdir -p /nuxt
WORKDIR /nuxt

RUN npm config set registry https://registry.npm.taobao.org

EXPOSE 9000

CMD ["bash", "/nuxt/run.sh"]
