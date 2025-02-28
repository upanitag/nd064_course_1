FROM python:3.8
LABEL maintainer="Katie Gamanji"

COPY . /app
RUN ls -l
WORKDIR /app
RUN ls -l
RUN pip install -r solutions/requirements.txt

# command to run on container start
CMD [ "python", "app.py" ]
