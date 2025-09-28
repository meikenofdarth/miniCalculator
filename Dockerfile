# Dockerfile

# Start with an official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local project files into the container's working directory
COPY . .

# Specify the command to run when the container starts
CMD ["python3", "app.py"]