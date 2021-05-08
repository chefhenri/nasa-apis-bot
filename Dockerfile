FROM python:3

ARG PORT=8080
ENV port $PORT

# Setup dependencies
WORKDIR .
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip list

COPY main.py ./
COPY apod ./apod
COPY botutils ./botutils

EXPOSE $port
CMD python3 main.py