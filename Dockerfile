FROM python:3.14

WORKDIR /app

RUN pip install flask

COPY flaskApp.py .

EXPOSE 5000

CMD ["flask", "--app", "flaskApp", "run", "--host=0.0.0.0"]