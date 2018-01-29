FROM ubuntu:latest
MAINTAINER Quilt Data, Inc. contact@quiltdata.io

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update && apt-get install -y \
    nginx \
    curl \
    gettext \
    libssl-dev
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -
RUN apt-get install -y nodejs
RUN apt-get install -y build-essential

RUN mkdir /opt/app
WORKDIR /opt/app

# Install dependencies
COPY package.json .
COPY internals internals
RUN ls
RUN pwd
VOLUME /opt/app/node_modules
RUN npm install --no-bin-links -y

# Install the app
COPY app app
COPY static static
COPY config.js.tmpl .
RUN npm install --global --no-bin-links rimraf -y || npm install --global --no-bin-links rimraf -y
RUN npm install --no-bin-links rimraf -y || npm install --no-bin-links rimraf -y
RUN npm run build

# Set up nginx
COPY nginx-web.conf /etc/nginx/sites-available/default
RUN rm -rf /usr/share/nginx/html
RUN cp -r /opt/app/build/ /usr/share/nginx/html/

# Substitute environment variables into config.js before starting nginx.
# Note: use "exec" because otherwise the shell will catch Ctrl-C and other signals.
CMD envsubst < config.js.tmpl > /usr/share/nginx/html/config.js && exec nginx -g 'daemon off;'
