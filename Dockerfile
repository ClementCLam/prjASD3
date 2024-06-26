# Use the official Jenkins LTS image as the base image
FROM jenkins/jenkins:lts

# Switch to the root user to install Python
USER root

# Update the package list and install Python and virtualenv
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Create a virtual environment and install pytest
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install --upgrade pip
RUN /opt/venv/bin/pip install pytest

# Switch back to the jenkins user
USER jenkins

# Expose the default Jenkins port
EXPOSE 8080

# Ensure the virtual environment is activated for all future commands
ENV PATH="/opt/venv/bin:$PATH"

# Start Jenkins
# ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/jenkins.sh"]
ENTRYPOINT ["/usr/bin/tini", "--", "/usr/local/bin/jenkins.sh"]