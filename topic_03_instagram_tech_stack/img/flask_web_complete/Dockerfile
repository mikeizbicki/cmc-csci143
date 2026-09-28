FROM ubuntu:24.04
# what does the above line mean?
# use the latest version of ubuntu, not 16.04

# a good principle:
# update the versions of the simplest software first;
# keep the more complex software at the same version

#MAINTAINER Mike Izbicki "mike@izbicki.me"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
# copies files from lambda server to the image/container

WORKDIR /app
# the /app folder doesn't exist in your git repo anywhere
# created automatically when the `docker build .` command is run
# you can think of /app as a "virtual" or "semantic" folder

RUN pip install -r requirements.txt
# recall that in regex ^ is begin of line (BOL) $ is EOL
# `ERROR: failed to solve` semantically means that the command had a failing exit code

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
