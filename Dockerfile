FROM python:3.9-slim

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    git \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install git+https://github.com/openai/whisper.git 
