FROM nginx:1.22

RUN mkdir -p /media && \
    mkdir -p /static && \
    mkdir -p /usr/share/nginx/ssl && \
    rm /etc/nginx/conf.d/default.conf

EXPOSE 80
EXPOSE 443
