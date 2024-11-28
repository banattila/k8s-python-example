FROM python:3.9

ADD . .

CMD ["ls", "python3", "src/main.py"]
