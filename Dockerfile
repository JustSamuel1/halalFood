FROM python:3.10.5-alpine
ENV PYTHONUNBUFFERD=1

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./meatFood /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]


