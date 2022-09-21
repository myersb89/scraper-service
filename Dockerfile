FROM python:3.9

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

COPY ./app /app

EXPOSE 9095 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app.main:app"]

