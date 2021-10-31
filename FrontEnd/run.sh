# !/bin/bash
npm config set proxy socks5://192.168.11.211:10808
npm config set https-proxy socks5://192.168.11.211:10808
npm install
npm run build && npm run start
