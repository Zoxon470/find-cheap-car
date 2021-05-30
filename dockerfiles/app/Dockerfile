FROM nginx/unit:1.23.0-python3.9

LABEL maintainer="Asadov Ahmed <zoxon470@gmail.com>"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PATH="${PATH}:/root/.poetry/bin"

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app

COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-dev

COPY dockerfiles/unit_config.json /docker-entrypoint.d/
COPY . .

EXPOSE 3000
