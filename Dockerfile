FROM python:3.12-slim

WORKDIR .

COPY app.py .

EXPOSE 8080

CMD ["python", "app.py"]

