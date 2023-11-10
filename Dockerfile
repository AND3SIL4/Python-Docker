FROM python:3

RUN mkdir -p /home/app

WORKDIR /home/app

COPY requirements.txt /home/app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/app

EXPOSE 8080

CMD ["python", "/home/app/app.py"]
