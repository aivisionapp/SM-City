FROM python:3.11-slim

RUN apt update
RUN apt install -y gcc

WORKDIR /usr/src/sm_city

COPY . .

RUN python -m pip install -r requirements.txt

CMD [ "python", "." ]
