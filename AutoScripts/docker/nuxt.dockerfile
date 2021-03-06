FROM node:16.11.1-buster

ENV NODE_ENV=production
ENV HOST=0.0.0.0

RUN mkdir -p /nuxt
WORKDIR /nuxt

EXPOSE 9000

CMD ["bash", "/nuxt/run.sh"]
