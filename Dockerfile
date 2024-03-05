FROM python:3.11.8-alpine3.19

ENV PYTHONUNBUFFERED 1 
ENV PYTHONDONTWRITEBYTECODE=1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
    && apk add libffi-dev py-cffi \
    && apk add gettext

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
