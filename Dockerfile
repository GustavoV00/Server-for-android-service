FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install aiohttp

EXPOSE 8080

CMD ["python", "app.py"]
