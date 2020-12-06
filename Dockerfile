# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/server

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements_prod.txt .
RUN pip install -r requirements_prod.txt

# copy entrypoint.sh
COPY ./entrypoint.prod.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/server/entrypoint.prod.sh"]