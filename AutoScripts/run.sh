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
echo "Ok!"

echo "Moving files..."
shopt -s extglob
cp -r $workdir/git/BackEnd/!(media) $workdir/django/
cp -r $workdir/git/FrontEnd/!(static) $workdir/nuxt/
shopt -u extglob
cp -r $workdir/git/FrontEnd/.nuxt $workdir/nuxt/

cp -r $workdir/git/BackEnd/media/* $workdir/media/
cp -r $workdir/git/FrontEnd/static/* $workdir/static/

cp -r $workdir/git/Config/mysql/* $workdir/mysql/
cp -r $workdir/git/Config/nginx/* $workdir/nginx/
echo "Ok!"

echo "Start run..."
cd $workdir/git/AutoScripts
docker-compose -f $workdir/git/AutoScripts/run.yml up
echo "Ok!"
