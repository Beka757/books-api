FROM python:3.10

WORKDIR /webapp

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /webapp/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /

COPY . .

ENTRYPOINT ["sh", "/entrypoint.sh"]