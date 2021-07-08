FROM nginx/unit:1.23.0-python3.9

LABEL maintainer="Asadov Ahmed <zoxon470@gmail.com>"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app

RUN pip install pipenv
COPY Pipfile* /tmp
RUN cd /tmp && pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY dockerfiles/app/unit_config.json /docker-entrypoint.d/config.json
COPY . .

EXPOSE 3000
