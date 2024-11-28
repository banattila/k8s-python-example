FROM python:3.9

ADD . .

CMD ["python3", "src/main.py"]
