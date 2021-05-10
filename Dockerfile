FROM python:3

# Setup dependencies
WORKDIR .
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip list

COPY main.py ./
COPY apod ./apod
COPY utils ./botutils
RUN mkdir ./logs

CMD python3 main.py