FROM python:3.9

ADD src/main.py .

CMD ["python3", "main.py"]
