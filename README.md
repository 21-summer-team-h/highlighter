# 📼 Highlighter

### Make Your Own Highlight Video Easily by Picking Up the Highlight Part of Your Twitch Video


> Highlighter is our web application project that helps you make a single highlight video by pulling out the five hottest clips from your video.

- **Analysis-Based**: We analysis chats and emotions of video. Highlight extraction is done by analyzing video comments. We use AI model to show you about emotions of each clip, so you can understand the video more easily and choose according to your preference.
- **Easy Select for Personalization**: You can pick up your favorite several clips and make highlight video with them. Emotion tags of each video would help you.
- **Just Link, Click, and Get Highlight Video!**: Link your twitch video, click to choose favorite clips, and get the final video. These are all we want from you to provide the best highlight video for you.
---
## Display flow
![display-flow](https://user-images.githubusercontent.com/55067949/127104148-62b15fde-6f45-4376-b95f-b542c65d570d.png)

---

## System Architecture
![System Architecture](https://user-images.githubusercontent.com/55067949/127111616-b2c3b050-cdc3-4351-925b-ba067ebcd9c1.png)

---

## Tech Stack
|Frontend|Backend|AI|DevOps|
|:------:|:---:|:---:|:---:|
|![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)<br>|![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)<br>![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)|![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)<br>![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)|![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)<br>![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)|


---

## Getting Started
### local
```bat
git clone https://github.com/21-summer-team-h/highlighter.git
cd highlighter
docker-compose up
```
now you can access to localhost in your browser! <br>

### browser
http://highlighter.shop

---

## Process
![process](https://user-images.githubusercontent.com/55067949/126746873-85131f1e-19e1-476b-a76f-ae4612c17991.jpg)

---

## References


### Open Source <br />
- [Twitch Video & Text Downloader](https://github.com/lay295/TwitchDownloader) - MIT License
- [Emotion recognition](https://github.com/omar178/Emotion-recognition) - MIT License
- [moviepy](https://github.com/Zulko/moviepy) - MIT License


### [API Specification](https://github.com/21-summer-team-h/highlighter/wiki)
### [Notion Design Docs](https://www.notion.so/Team-H-Docs-f162f52cb49c486f9a1b97cf17767a3a)

---

## Docker images
link to docker hub

### [Frontend](https://hub.docker.com/repository/docker/ks0624/highlighter-frontend)
```bat
ks0624/highlighter-frontend
```
### [Backend](https://hub.docker.com/repository/docker/ks0624/highlighter-backend)
```bat
ks0624/highlighter-backend
```
### [Nginx](https://hub.docker.com/repository/docker/ks0624/highlighter-nginx)
```bat
ks0624/highlighter-nginx
```


---
## Team
> **Twitch Video Highlighter Web Project**
>
> 2021.06.28 ~ 2021.07.30
>
>

|김서경 <br> Seokyung Kim|김재훈 <br> Jaehun Kim|문수인 <br> Sooin Moon|장예서 <br> Yeseo Jang|채지은 <br> Chae Jieun|
|:---:|:---:|:---:|:---:|:---:|
|Backend<br>DevOps|Backend<br>DevOps|Frontend<br>AI|Backend<br>DevOps|Frontend<br>AI|
