# pull official base image
FROM python:3.12.2-slim

# set work directory
WORKDIR /usr/src/website

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat-openbsd

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/website/
RUN sed -i 's/\r$//g' /usr/src/website/entrypoint.sh
RUN chmod +x /usr/src/website/entrypoint.sh

# copy project
COPY . .

EXPOSE 8000

# run entrypoint.sh
ENTRYPOINT ["/usr/src/website/entrypoint.sh"]