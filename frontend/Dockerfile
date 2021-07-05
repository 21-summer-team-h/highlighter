# Nginx가 제공 해줄 Build 파일 생성 단계
FROM node:alpine as builder
WORKDIR /app
COPY ./package.json ./
RUN npm install
COPY . .
# RUN npm run build

# NginX를 가동하고 생성된 빌드 파일 제공. default.conf에서 해준 설정을
FROM nginx
EXPOSE 3000
# 원래 있던 걸 우리가 작성한 걸로 덮어씌우는 과정
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
# 빌드파일들을 nginx root로 보냄
COPY --from=builder /app/build /usr/share/nginx/html