FROM gitpod/workspace-mysql

RUN mkdir /application
WORKDIR "/application"
# Upgrade pip
RUN pip install --upgrade pip
# Update
RUN apt-get update \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/* 
# Installere Requirements
COPY . /application
RUN pip install -r requirements.txt
CMD [ "python" ]
