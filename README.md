# Server-for-android-service

Essa aplicação é para receber os dados de um serviço de accessbilidade Android (https://github.com/GustavoV00/android-app-test) com o intuito de gerar logs.

## How to run

docker build -t nginx_image_name nginx -> This builds a nginx image <br/>
docker run -d -p PORT:PORT nginx_image_name -> This runs the image <br/>
gunicorn app:my_web_app --bind localhost:PORT --worker-class aiohttp.GunicornWebWorker -> To run the server <br/>
-> Para mais workers, use a flag -w, exemplo: -w 4
