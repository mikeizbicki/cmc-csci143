FROM postgres:12

RUN apt-get update && apt-get install -y \
    less \
    make \
    vim

RUN mkdir /tmp/sql_quiz
COPY . /tmp/sql_quiz
WORKDIR /tmp/sql_quiz

# copy over the pagila database;
# we rename the files so that they get executed in the correct order
COPY ./create_tables.sql /docker-entrypoint-initdb.d/01.sql
