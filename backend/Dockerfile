FROM python:3.11.0-slim

RUN apt update
RUN apt install -y gcc

WORKDIR /usr/src/sm_city

COPY . .

RUN python -m pip install -e requirements.txt

CMD [ "python", "." ]
