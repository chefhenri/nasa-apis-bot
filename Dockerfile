FROM python

ARG PORT=8080

ENV port $PORT

WORKDIR .
COPY main.py ./

RUN pip list

CMD python3 main.py