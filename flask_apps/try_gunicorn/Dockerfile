FROM python:3.6

ADD . /app

WORKDIR /app

RUN pip install flask gunicorn

EXPOSE 5000

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]