Vagrant.configure("2") do |config|

  config.vm.box = "bento/ubuntu-16.04"

  config.vm.network "forwarded_port", guest: 22, host: 2223, auto_correct: true, id: "ssh"
  config.vm.network "forwarded_port", guest: 7501, host: 7501

  config.vm.synced_folder "./", "/vagrant_data"

  config.vm.provision "shell", path: "https://get.docker.com/"

  config.vm.provision "shell", inline: <<-SHELL
    sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    sudo systemctl enable docker
    sudo systemctl start docker
    sudo usermod -aG docker $USER
    newgroup docker
    docker run hello-world
  SHELL

  config.vm.provision "shell", inline: <<-SHELL\
    sudo docker-compose -f /vagrant/docker-compose.yaml up -d
  SHELL
end
