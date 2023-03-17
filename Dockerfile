FROM ubuntu:latest

# Install required packages
RUN apt-get update && \
    apt-get install -y python3-pip python3-dev && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install scala --yes

# Set environment variables
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/

# Install Python packages
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install Flask
RUN pip install requests
RUN pip install jsonify
RUN pip install flask_cors

COPY . .

EXPOSE 5000

# Start the Flask app
ENTRYPOINT ["flask", "run","--host", "0.0.0.0"]
#"--host", "0.0.0.0"
