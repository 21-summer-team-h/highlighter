FROM node:alpine

WORKDIR /app

COPY ./package.json ./

RUN apt-get install curl

RUN npm install

COPY . .

RUN chmod +x TwitchDownloader.sh

CMD npm run start

VOLUME /home/volume/video
