FROM python:3.10.6-alpine3.16

RUN apk update && apk upgrade && apk add --update busybox-suid

WORKDIR /adituu.dev

COPY requirements.txt .

RUN python -m pip install --upgrade pip && pip install -r requirements.txt && rm -rf requirements.txt

RUN mkdir -p log/

COPY . .

CMD [ "python", "server.py" ]
