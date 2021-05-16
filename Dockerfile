FROM python:3

ENV MODE prod
ENV VENV /opt/venv

# Setup environment
WORKDIR .
RUN mkdir ./logs

# Setup virtual environment
RUN python3 -m venv $VENV
ENV PATH "$VENV/bin:$PATH"

# Setup dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy files
COPY main.py .
COPY utils ./utils
COPY apod ./apod

ENTRYPOINT python3 main.py $MODE