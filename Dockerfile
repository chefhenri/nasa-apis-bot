FROM python:3

ENV MODE prod

# Setup dependencies
WORKDIR .
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip list

COPY main.py .
COPY utils ./utils
COPY apod ./apod

RUN mkdir ./logs

ENTRYPOINT python3 main.py $MODE