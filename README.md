Docker is an open platform for devloping, shipping and running applications. Docker enables to separate applications from infrastructure.

Docker provides the ability to package and run an application in a loosely isolated environment called a container.
Docker uses host OS kernel, there is no custom or additional kernel inside container. All containers which run on a machine are sharing this host kernel they doesn't require OS exclusively.

Setup Docker on Ubuntu based environment:
-------------------------------------------
#Installation through curl:
    sudo apt install curl
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh

Run Docker as a non-root user: 
--------------------------------
If you would like to use Docker as a non-root user, you should now consider adding your user to the “docker” group with something like:
    sudo usermod -aG docker $USER
After adding user either log out and back in for this to take effect or source ~/.bashrc
