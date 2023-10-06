# Use an official Nginx image as the base image
FROM nginx:latest

# Copy your Nginx configuration file into the container
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 for incoming HTTP traffic
EXPOSE 80

# Start Nginx when the container is run
CMD ["nginx", "-g", "daemon off;"]