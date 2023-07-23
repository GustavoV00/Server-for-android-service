from flask import Flask, request, Response
from utils import log

app = Flask(__name__)
logger = log.RotatingLogger(
    "log/log_file",
)

response_content = "Ok"
status_code = 200
response_headers = {"Content-Type": "text/plain"}


@app.route("/windows", methods=["POST"])
def save_windows():
    data = request.json
    logger.info(data)

    return Response(response_content, status=status_code, headers=response_headers)


if __name__ == "__main__":
    app.run()
