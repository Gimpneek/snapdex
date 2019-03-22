FROM python:3.7

# Set up environment variable for the discord key
ENV DISCORD_KEY=replace_me

# Create directory to run everything in
RUN mkdir /src
WORKDIR /src

# Add source files to directory
ADD . /src
RUN pip install -r requirements.txt

# Run Python
ENTRYPOINT ["python", "snapdex_discord_bot.py"]
