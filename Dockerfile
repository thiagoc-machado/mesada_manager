FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/

RUN python -m venv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]