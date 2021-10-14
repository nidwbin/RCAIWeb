# !/bin/bash
workdir=/RCAIWeb/

function install_docker(){
        cp /etc/apt/sources.list /etc/apt/sources.list.bak
        sed -i s/archive.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g /etc/apt/sources.list
        apt update && apt install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
        
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
        curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
        
        chmod +x /usr/local/bin/docker-compose
        echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
        
        apt update && apt install -y docker-ce docker-ce-cli containerd.io
}

function install_others() {
    echo "Installing other dependencies..."
    git --version
    if [ ! $? -eq 0 ]; then
        echo "Installing git..."
        apt update && apt install -y git
    fi
    echo "Ok!"
}

function check() {
    echo "Change apt sources..."
    cp /etc/apt/sources.list /etc/apt/sources.list.bak
    sed -i s/archive.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g /etc/apt/sources.list
    echo "Ok!"

    echo "Checking docker..."
    docker -v
    if [ $? -eq 0 ]; then
        echo "Docker installed."
    else
        echo "!!!Warining: I am trying to install docker!!!"
        install_docker
    fi
    install_others
}

echo "!!!Must run by root!!!"
echo "!!!Script for frist run!!!"
echo "!!!If not, please stop with Ctrl+C now!!!"
sleep 20

# check

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
shopt -u extglob
cp -r $workdir/git/FrontEnd/.nuxt $workdir/nuxt/
cp -r $workdir/git/FrontEnd/package.json $workdir/nuxt/
cp -r $workdir/git/FrontEnd/package-lock.json $workdir/nuxt/
cp -r $workdir/git/BackEnd/media/* $workdir/media/
cp -r $workdir/git/FrontEnd/static/* $workdir/static/
cp -r $workdir/git/Config/mysql/* $workdir/mysql/
cp -r $workdir/git/Config/nginx/* $workdir/nginx/
cp $workdir/django/requirements.txt $workdir/git/AutoScripts/docker/
cp $workdir/nuxt/package.json $workdir/git/AutoScripts/docker/
echo "Ok!"

echo "Start run..."
cd $workdir/git/AutoScripts
docker-compose -f $workdir/git/AutoScripts/run.yml up
echo "Ok!"
