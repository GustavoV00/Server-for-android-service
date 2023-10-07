# Server-for-android-service

Essa aplicação é para receber os dados de um serviço de accessbilidade Android (https://github.com/GustavoV00/android-app-test) com o intuito de gerar logs.

## How to run

docker build -t image_name . <br/>
docker run -p 5000:5000 image_name -> Needs to be port 5000, because it's where nginx is running

### Dependencies
