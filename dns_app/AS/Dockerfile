FROM python:3.5

RUN apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*




RUN pip install Flask
COPY run.py ./


CMD [ "python", "./run.py" ]
