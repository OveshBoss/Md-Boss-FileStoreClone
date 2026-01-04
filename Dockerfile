# Don't Remove Credit @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

# Buster ki jagah Bullseye use karein, ye stable hai
FROM python:3.10-slim-bullseye

# System packages install karein (Optimization ke saath)
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y git python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Requirements pehle copy karein taaki cache use ho sake
COPY requirements.txt /requirements.txt

# Pip upgrade aur requirements install karein
RUN pip3 install -U pip && pip3 install --no-cache-dir -U -r /requirements.txt

# Workdir setup karein
WORKDIR /VJ-File-Store
COPY . /VJ-File-Store

# Bot start karein
CMD ["python3", "bot.py"]
