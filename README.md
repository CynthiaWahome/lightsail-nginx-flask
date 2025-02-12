```markdown
# AWS Lightsail Nginx Reverse Proxy with Flask

[![AWS](https://img.shields.io/badge/AWS-Lightsail-orange?logo=amazon-aws)](https://aws.amazon.com/lightsail/)
[![Docker](https://img.shields.io/badge/Docker-Containers-blue?logo=docker)](https://www.docker.com/)
[![Nginx](https://img.shields.io/badge/Server-Nginx-brightgreen?logo=nginx)](https://nginx.org/)

A production-ready template for deploying a Flask web server behind an Nginx reverse proxy on AWS Lightsail Containers.

---

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup & Deployment](#setup--deployment)
- [Logging & Monitoring](#logging--monitoring)
- [Cleanup](#cleanup)
- [FAQ](#faq)
- [License](#license)

---

## Overview
Deploy a secure, scalable Flask app with:
- **Nginx Reverse Proxy**: Routes traffic to Flask and hides backend details.
- **AWS Lightsail Containers**: Managed Docker hosting with simplicity.
- **Isolated Environments**: Separate containers for proxy and app logic.

---

## Prerequisites
- AWS Account
- AWS CLI + [Lightsail Control Plugin](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-install-software)
- Docker

---

## Setup & Deployment

### 1. Clone the Repository
```bash
git clone https://github.com/CynthiaWahome/lightsail-nginx-flask.git
cd lightsail-nginx-flask
```

### 2. Build and Test Locally
```bash
# Build Flask
docker build -t flask-container ./flask

# Build Nginx
docker build -t nginx-container ./nginx

# Run containers
docker run -d -p 5000:5000 --name flask-app flask-container
docker run -d -p 80:80 --name nginx-proxy --link flask-app nginx-container
```

### 3. Deploy to AWS Lightsail
```bash
# Create service
aws lightsail create-container-service \
  --service-name my-service \
  --power small \
  --scale 1

# Push images (replace X/Y with your versions)
aws lightsail push-container-image \
  --service-name my-service \
  --label flask-container \
  --image flask-container

aws lightsail push-container-image \
  --service-name my-service \
  --label nginx-container \
  --image nginx-container

# Deploy
aws lightsail create-container-service-deployment \
  --service-name my-service \
  --containers file://containers.json \
  --public-endpoint file://public-endpoint.json
```

---

## Logging & Monitoring
```bash
# Nginx logs
aws lightsail get-container-log \
  --service-name my-service \
  --container-name sample-nginx \
  --log-type "nginx-access"

# Flask logs
aws lightsail get-container-log \
  --service-name my-service \
  --container-name sample-flask \
  --log-type "flask"
```

---

## Cleanup
```bash
aws lightsail delete-container-service --service-name my-service
```

---

## FAQ
**Q: Why 502 Bad Gateway?**  
A: Check `FLASK_HOST` in `containers.json` matches the Flask container name.

**Q: How to add HTTPS?**  
A: Configure SSL in Nginx and use AWS Certificate Manager (ACM).

---

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more details.