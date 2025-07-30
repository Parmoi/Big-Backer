FROM python:3.13.3-slim

# Copy and install application dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download wait-for-it.sh
RUN apt-get update && apt-get install -y curl && \
    curl -o /wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x /wait-for-it.sh && \
    apt-get remove -y curl && apt-get autoremove -y && apt-get clean

# Copy the rest of the code
COPY . .
EXPOSE 5000

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

# Use wait-for-it.sh to wait for the DB to be ready before we launch our app
# wait-for-it.sh check if port is ready for connection
CMD ["/wait-for-it.sh", "db:5432", "--", "python", "run.py"]