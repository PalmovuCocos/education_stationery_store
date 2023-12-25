# создание образа на основе python
FROM python:3.11

# установка виртуальных переменных
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# создание рабочей директории
WORKDIR /usr/src/stationery_store/globus

# выполнение команды
RUN pip install --upgrade pip
RUN pip install pipenv
# копирование и установка requirements
COPY ./Pipfile /usr/src/
COPY ./Pipfile.lock /usr/src
COPY ./.env /usr/src/stationery_store

ENV PIPENV_VENV_IN_PROJECT=1

RUN cd /usr/src/ && pip install --user --upgrade pipenv
RUN cd /usr/src/ && pipenv install
RUN cd /usr/src/ && pipenv install --system

# копирование всего проекта
COPY ./globus /usr/src/stationery_store/globus