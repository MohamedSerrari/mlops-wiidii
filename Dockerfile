FROM python:3.7.9

WORKDIR /app
ADD . /app

RUN pip3 install --upgrade pip
RUN pip install -r ./requirements.txt

EXPOSE 8080

CMD ["main.py"]
