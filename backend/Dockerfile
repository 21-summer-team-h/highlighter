FROM node

WORKDIR /app

VOLUME /app

COPY ./package.json ./

RUN npm install

COPY ./TwitchDownloader.sh /home/video
COPY ./TwitchDownloaderCLI /home/video

COPY . .

RUN chmod +x TwitchDownloaderCLI

RUN chmod +x TwitchDownloader.sh

RUN npm run start
