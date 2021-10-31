# !/bin/bash
if [ -f ./env.tar.gz ]; then
  tar -xzvf env.tar.gz
else
  npm install
fi
npm run build && npm run start
