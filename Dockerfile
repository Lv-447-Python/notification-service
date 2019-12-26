FROM python:3
ENV PYTHONBUFFERED 1
RUN mkdir /notification_service
WORKDIR /notification_service
COPY . /notification_service/
RUN make setup_docker