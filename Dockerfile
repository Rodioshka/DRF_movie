FROM python:3.8

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONNUNBUFFERED 1

WORKDIR /usr/src/dm_rest

COPY ./requirements.txt /usr/srs/requirements.txt
RUN pip install -r /usr/srs/requirements.txt

COPY . /usr/src/dm_rest

#EXPOSE 8000
#CMD ["python", "manage.py", "migrate"]
#CMD ["python", "manage.py","runserver", "0.0.0.0:8000"]