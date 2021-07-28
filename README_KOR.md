# 📼 Highlighter

### 나만의 Twitch 하이라이트 비디오를 쉽게 만들 수 있습니다.


> Highlighter는 비디오에서 가장 핫한 클립 5개를 뽑아 하나의 하이라이트 비디오를 만들 수 있도록 도와주는 웹 애플리케이션 프로젝트입니다.

- **Analysis-Based**: 우리는 영상의 채팅과 감정을 분석합니다. 하이라이트 추출은 동영상 채팅 수를 분석하여 수행됩니다. AI 모델을 사용하여 각 클립의 감정을 보여주므로 동영상을 보다 쉽게 이해하고 기호에 따라 선택할 수 있습니다.

- **Easy Select for Personalization**: 마음에 드는 클립을 골라 하이라이트 영상을 만들 수 있습니다. 각 영상의 감정 태그가 도움이 될 것입니다.

- **Just Link, Click, and Get Highlight Video!**: 트위치 비디오의 링크를 입력하고 마음에 드는 클립을 선택하여 클릭한 다음 최종 비디오를 얻을 수 있습니다.
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

## 시작하기
### local
```bat
git clone https://github.com/21-summer-team-h/highlighter.git
cd highlighter
docker-compose up
```
이제 브라우저에서 localhost에 액세스할 수 있습니다! <br>

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


### [API 명세](https://github.com/21-summer-team-h/highlighter/wiki)
### [Notion Design Docs](https://www.notion.so/Team-H-Docs-f162f52cb49c486f9a1b97cf17767a3a)

---

## Docker images
도커 허브

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
|Backend<br>DevOps|Backend|Frontend<br>AI|Backend<br>DevOps|Frontend<br>AI|
