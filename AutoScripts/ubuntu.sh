# !/bin/bash


function install_docker(){
        apt install -y ca-certificates curl gnupg-agent software-properties-common
        
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
        curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
        
        chmod +x /usr/local/bin/docker-compose
        echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
        
        apt update && apt install -y docker-ce docker-ce-cli containerd.io && systemctl enable docker
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
    apt update && apt install -y python wget apt-transport-https
    wget https://tuna.moe/oh-my-tuna/oh-my-tuna.py
    python oh-my-tuna.py --global
    apt update
    echo "Ok!"

    echo "Checking docker..."
    docker -v
    if [ $? -eq 0 ]; then
        echo "Docker installed."
    else
        echo "!!!Warning: I am trying to install docker!!!"
        install_docker
    fi
    install_others
}

echo "!!!Must run by root!!!"
echo "!!!Script for first run!!!"
echo "!!!If not, please stop with Ctrl+C now!!!"
sleep 20

check

if [ -f ./run.sh ]; then
  bash ./run.sh
else
  echo "!!!Error: there is not run.sh in here!!!"
fi

