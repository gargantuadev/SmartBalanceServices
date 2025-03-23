# Use an official lightweight Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8080

# Set environment variables (if needed)
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# Start the Flask application using gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "api:create_app"]
