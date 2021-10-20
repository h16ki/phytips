# build stage
FROM python:3.9-bullseye as build

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apt-get update && \
    apt-get install -y nodejs && \
    python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt && \
    rm -rf ~/.cache


# production stage
FROM python:3.9-slim-bullseye as production

COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
# RUN apt-get update && apt-get install -y git && \
#     apt-get install -y nodejs && \
#     curl https://cli-assets.heroku.com/install.sh | sh

WORKDIR /

WORKDIR /app
ENTRYPOINT [ "/bin/bash" ]
VOLUME "/app"
