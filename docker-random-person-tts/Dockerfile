# Use an official Python runtime as a parent image
# FROM python:3.8-slim-buster

# # Set the working directory to /app
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # aplay utility must be installed within the Docker image
# RUN apt-get install -y alsa-utils

# # Install any needed packages specified in requirements.txt
# RUN apt-get update && apt-get install -y mpg321 
# RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# # Install PulseAudio codebase since MacOs requires additional setup 
# # steps, including running a PulseAudio server within the container 
# # and configuring audio forwarding.
# # RUN apt-get update && apt-get install pulseaudio
# # Copy PulseAudio client configuration
# COPY pulse-client.conf /etc/pulse/client.conf

# # Run the script when the container launches
# CMD ["python", "random_person_tts.py"]

# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster
# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script to the container
COPY 01-ConnieIntro.py .

# Run the Python script when the container starts
CMD ["python", "01-ConnieIntro.py"]


