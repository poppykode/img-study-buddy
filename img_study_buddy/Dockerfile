FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
WORKDIR /app
#COPY requirements.txt /app
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "sh","entrypoint.sh" ]
