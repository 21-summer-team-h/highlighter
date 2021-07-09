FROM node:alpine

WORKDIR /app

COPY ./package.json ./

RUN npm install

#RUN chmod +x TwitchDownloader.sh

COPY . .

CMD node mysql.js


#VOLUME /home/volume/video