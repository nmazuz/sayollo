# Set the base image to Ubuntu
FROM ubuntu

# Update the repository sources list and install gnupg2
RUN apt-get update && apt-get install -y gnupg2

# Add the package verification key
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10

# Add MongoDB to the repository sources list
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' > tee /etc/apt/sources.list.d/mongodb.list

# Update the repository sources list
RUN apt-get update

# Install MongoDB package (.deb)
RUN apt-get install -y mongodb

# Create the default data directory
RUN mkdir -p /data/db

# Define default command.
CMD ["mongod"]

# Expose ports.
#   - 27017: process
#   - 28017: http
EXPOSE 27017
EXPOSE 27018