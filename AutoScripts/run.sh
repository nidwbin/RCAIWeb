# !/bin/bash
workdir=/RCAIWeb/
# mkdir -p $workdir
# git clone git@github.com:nidwbin/RCAIWeb.git $workdir/git

echo "Make dirs..."
mkdir -p $workdir/django
mkdir -p $workdir/nuxt
mkdir -p $workdir/mysql
mkdir -p $workdir/nginx
mkdir -p $workdir/media
mkdir -p $workdir/static

mkdir -p $workdir/mysql/conf.d
mkdir -p $workdir/mysql/init
mkdir -p $workdir/mysql/data
mkdir -p $workdir/mysql/logs
mkdir -p $workdir/nginx/log
mkdir -p $workdir/nginx/ssl
echo "Ok!"

echo "Moving files..."
cp -ar $workdir/git/BackEnd/ $workdir/django/
cp -ar $workdir/git/FrontEnd/ $workdir/nuxt/
cp -ar $workdir/git/Config/mysql/* $workdir/mysql/
cp -ar $workdir/git/Config/nginx/* $workdir/nginx/

mv $workdir/django/media/ $workdir/media/
mv $workdir/nuxt/static/static/ $workdir/static/
echo "Ok!"

echo "Start run..."
cd $workdir/git/AutoScripts
docker-compose -f $workdir/git/AutoScripts/run.yml up
echo "Ok!"
