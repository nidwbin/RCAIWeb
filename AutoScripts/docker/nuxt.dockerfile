FROM node:16.15.0-buster

ENV NODE_ENV=production
ENV HOST=0.0.0.0

RUN mkdir -p /nuxt
WORKDIR /nuxt

EXPOSE 9000

CMD ["bash", "/nuxt/run.sh"]
