FROM python:3.11-alpine

WORKDIR /app

RUN apk update && apk add ffmpeg

COPY ./src .

CMD ["python3", "main.py"]
