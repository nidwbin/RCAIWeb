# !/bin/bash
function check_docker() {
    echo "Checking docker..."
    docker -v
    if [ $? -eq 0 ]; then
        echo "Docker installed."
        return 0
    else
        echo "Error: please install docker!"
        return 1
    fi
}

function install_dep() {
    echo "Installing dependencies..."
    check_docker
    if [ $? -eq 0 ]; then
        echo "Installing make git..."
        sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
        sudo sed -i s/archive.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g /etc/apt/sources.list
        sudo apt update && apt install -y make git 
    fi
}

installed_dep

git clone git@github.com:nidwbin/RCAIWeb.git

make build
make run
