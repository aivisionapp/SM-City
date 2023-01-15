FROM python:3.11.0-slim

RUN apt update
RUN apt install -y gcc

WORKDIR /usr/src/sm_city

COPY . .

CMD [ "python", "-m", "http.server" ]
