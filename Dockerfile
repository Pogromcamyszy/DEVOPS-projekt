#Use a base image with Linux
FROM debian:bullseye-slim

#Update package and install Python and Nginx
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    nginx \
    && rm -rf /var/lib/apt/lists/*

#Set up a workdir for app
WORKDIR /app2

#Copy application code to workdir
COPY ./app /app2  

#Install Python dependencies 
RUN pip3 install --no-cache-dir -r /app2/req.txt  

#Remove the default Nginx site configuration
RUN rm /etc/nginx/sites-enabled/default

#Copy the Nginx config file 
COPY ./nginx.conf /etc/nginx/nginx.conf

#Expose port 80 for Nginx which will proxy flask
EXPOSE 80

#Command to start Flask and Nginx
CMD ["sh", "-c", "python3 /app2/app.py & exec nginx -g 'daemon off;'"]
