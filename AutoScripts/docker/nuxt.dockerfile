FROM node:latest

ENV NODE_ENV=production
ENV HOST=0.0.0.0

RUN mkdir -p /nuxt
WORKDIR /nuxt

RUN npm config set registry https://mirrors.huaweicloud.com/repository/npm/

EXPOSE 9000

CMD ["bash", "/nuxt/run.sh"]
