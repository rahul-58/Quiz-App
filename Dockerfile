# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file first (helps with caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project (including run.py) into the container
COPY . .

# Expose Flask's default port
EXPOSE 5000

# Run the Flask app (since run.py is at the root, we call it directly)
CMD ["python", "run.py"]
