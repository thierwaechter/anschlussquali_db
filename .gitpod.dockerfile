FROM gitpod/workspace-mysql

RUN sudo apt-get update \
 && sudo apt-get install -y \
    tool \
 && sudo rm -rf /var/lib/apt/lists/*

RUN sudo mkdir /application
WORKDIR "/application"
# Upgrade pip
RUN sudo pip install --upgrade pip

# Installere Requirements
COPY sudo . /application
RUN sudo pip install -r requirements.txt
CMD [ "python" ]
