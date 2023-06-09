# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install mpg321 and necessary audio dependencies
RUN apt-get update && apt-get install -y mpg321 libasound2-dev alsa-utils

# Copy the requirements file and install the dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python program to the container
COPY 01-ConnieIntro.py .

# Run the Python program
CMD [ "python", "01-ConnieIntro.py" ]


