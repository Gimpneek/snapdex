FROM python:3.7

LABEL version="1.0.2"
LABEL description="Discord bot to create a pokedex from Pokemon Go AR pics"

# Set up environment variable for the discord key
ENV DISCORD_KEY=replace_me

# Create directory to run everything in
RUN mkdir /src
WORKDIR /src

# Add source files to directory
ADD . /src
RUN pip install -r requirements.txt

# Run Python
ENTRYPOINT ["python", "main.py"]
