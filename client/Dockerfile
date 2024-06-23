# Use official Python image as base
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy current directory into /app in container
COPY . /app

# Make port 9999 available outside this container
# EXPOSE 9999

# Run the client script when the container starts
CMD ["python", "client.py"]