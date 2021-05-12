FROM python:3

# Setup dependencies
WORKDIR .
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip list

COPY utils apod ./
RUN mkdir ./logs

CMD python3 main.py