# syntax=docker/dockerfile:1.7.0

FROM python:3.11.10-slim

WORKDIR /app

COPY github_reporting_tool.py .
COPY requirements.txt .

RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir -r requirements.txt

ARG UID=1000
ARG GID=1000

RUN groupadd -g "${GID}" python \
    && useradd --create-home \
               --no-log-init \
               -u "${UID}" \
               -g "${GID}" \
               python

ENV PATH=/home/python/.local/bin:$PATH

USER python

CMD [ "python", "github_reporting_tool.py" ]
