FROM python:3.8.5-alpine

RUN apk add --no-cache gcc musl-dev

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./django_deploy /app

WORKDIR /app


COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]