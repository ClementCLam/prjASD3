# Use the official Jenkins LTS image as the base image
FROM jenkins/jenkins:lts

# Switch to the root user to install Python
USER root

# Update the package list and install Python
RUN apt-get update && apt-get install -y python3 python3-pip

# Switch back to the jenkins user
USER jenkins

# Expose the default Jenkins port
EXPOSE 8080

# Start Jenkins
# ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/jenkins.sh"]
ENTRYPOINT ["/usr/bin/tini", "--", "/usr/local/bin/jenkins.sh"]