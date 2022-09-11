FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN mkdir mediafiles
RUN mkdir staticfiles
RUN chown root.root ./mediafiles
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/