FROM node:alpine

WORKDIR /app

COPY ./package.json ./

RUN npm install

RUN chmod +x TwitchDownloader.sh

COPY . .

CMD npm run start

VOLUME /home/volume/video