FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /fastapi

COPY poetry.lock pyproject.toml ./

RUN pip3 install poetry && poetry config virtualenvs.create false && poetry install

COPY . ./

CMD python manage.py runserver