FROM python:3.10
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Set host to 0.0.0.0 to make it run on the container's network
CMD uvicorn app:app --host 0.0.0.0