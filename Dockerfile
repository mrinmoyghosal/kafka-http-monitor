FROM python:3.9-slim
COPY . /app
ENV PYTHONPATH /app/
ENV POETRY_VERSION 1.1.4
# install poetry
RUN pip install "poetry==$POETRY_VERSION"
WORKDIR /app

# instal git and build tools for librdkafka
RUN apt-get update && apt-get install -y git gcc build-essential
RUN git clone https://github.com/edenhill/librdkafka
WORKDIR /app/librdkafka/
RUN ls -l
RUN ./configure
RUN make
RUN make install
RUN ldconfig

# install the application
WORKDIR /app
RUN rm -rf librdkafka
RUN poetry install
RUN ls -l
RUN poetry run pytest tests
RUN poetry run python setup.py install