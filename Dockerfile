# Use an official Python image as the base image
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy your application code and requirements file into the container
COPY app.py /app/
COPY utils/ /app/utils/
COPY requirements.txt /app/

# Install application dependencies
RUN pip install -r requirements.txt

# Install Nginx
RUN apt-get update && apt-get install -y nginx supervisor

# Copy the configuration files
COPY configs/nginx.conf /etc/nginx/nginx.conf
COPY configs/supervisord-gunicorn.conf /etc/supervisor/conf.d/

# Expose port 5000 for Nginx
EXPOSE 5000

# Copy the startup script into the container
COPY scripts/start-gunicorn.sh /app/
RUN chmod +x /app/start-gunicorn.sh

# Command to run the startup script
CMD ["supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]