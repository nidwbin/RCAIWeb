FROM nginx:latest

RUN mkdir -p /media && \
    mkdir -p /static && \
    mkdir -p /usr/share/nginx/ssl

EXPOSE 80
EXPOSE 443
