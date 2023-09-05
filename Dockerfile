FROM python:3.8-slim-buster
ARG UID=1000
ARG GID=1000

RUN groupadd -g "${GID}" python \
  && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" python

USER python
WORKDIR /app
COPY requirements.txt requirements.txt
ENV PATH=/home/python/.local/bin:$PATH
RUN pip3 install -r requirements.txt
COPY github_reporting_tool.py github_reporting_tool.py
CMD [ "python3","github_reporting_tool.py" ]
