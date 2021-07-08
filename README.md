# find-cheap-car
Service for finding a cheap car

### How to run
```sh
$ git clone https://github.com/Zoxon470/find-cheap-car && cd find-cheap-car
$ cp .env.example .env
$ docker-compose up --build -d # Running all service
$ docker-compose exec app alembic upgrade head # Migrating database
```

### Environment variables

| Key    | Description   |    Example value  |
| :---         |     :---      |          :--- |
| `DATABASE_URI`  | Database URI | postgresql+asyncpg://find-cheap-car:find-cheap-car@db:5432/find-cheap-car              |
| `REDIS_HOST`  | Redis host  | redis              |
| `REDIS_PORT`  | Redis port  | 6379              |
| `POSTGRES_USER`  | Postgres user  | find-cheap-car              |
| `POSTGRES_PASSWORD`  | Postgres password  | find-cheap-car              |
| `POSTGRES_DB`  | Postgres database name  | find-cheap-car              |
