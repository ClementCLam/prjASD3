# Use official Python image as base
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory into the container
#COPY server.py .
#COPY server_config.json .
COPY . /app

# Install any dependency packages specified in requirement.txt file
# RUN pip install -r requirements.txt

# Run the server script when the container starts
CMD ["python", "server.py"]