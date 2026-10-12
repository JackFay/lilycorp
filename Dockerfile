FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY portal/requirements.txt /app/portal/requirements.txt
RUN pip install --no-cache-dir -r /app/portal/requirements.txt

# Copy repository content
COPY . /app/

ENV PORT=8080
ENV PYTHONUNBUFFERED=1

EXPOSE 8080

CMD ["python", "portal/server.py"]
