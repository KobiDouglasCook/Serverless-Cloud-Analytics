# Serverless URL Shortener with Real‑Time Analytics

A globally distributed, production‑grade serverless application built on AWS. This project demonstrates advanced cloud architecture, multi‑origin CloudFront routing, event‑driven analytics, Infrastructure‑as‑Code with AWS SAM, and a fully automated deployment workflow suitable for real-world production environments.

This repository is designed as a portfolio‑quality example of cloud engineering, emphasizing scalability, security, cost optimization, and operational excellence.


<img width="1056" height="946" alt="000" src="https://github.com/user-attachments/assets/a23f2954-214d-4273-b015-f5283f184e09" />





---

# Overview

This project implements a serverless URL shortener with real‑time analytics. Users can generate short URLs, redirect through CloudFront, and view analytics such as click counts and event logs. The system is globally distributed, highly available, and designed for minimal operational overhead.

Key features:

- Short URL creation via API Gateway and Lambda  
- Global redirection through CloudFront  
- Event‑driven analytics pipeline using EventBridge  
- DynamoDB tables for URLs and analytics events  
- Static frontend hosted on S3 + CloudFront  
- CloudFront multi‑origin routing for clean URLs  
- Fully automated deployment using AWS SAM  
- Zero manual console configuration after initial setup  

---

# Architecture

The system is composed of several AWS services working together to deliver a globally distributed, highly scalable application.

## Components

### Frontend
- Static site hosted in S3  
- Served globally through CloudFront  
- Routes:
  - `/` – main UI  
  - `/analytics.html` – analytics dashboard  

### Backend APIs (API Gateway + Lambda)
- `POST /shorten` – create short URLs  
- `GET /r/{shortCode}` – redirect handler  
- `GET /analytics/{shortCode}` – analytics API  

### Data Storage
- DynamoDB table `UrlTable` for URL mappings  
- DynamoDB table `AnalyticsEvent` for click events  

### Event Processing
- EventBridge rule triggers analytics processor Lambda  
- Analytics processor writes events to DynamoDB  

### Global Distribution Layer
- CloudFront distribution with multiple origins:
  - S3 origin for frontend  
  - API Gateway origin for backend  
- CloudFront behaviors route:
  - `shorten` → API Gateway  
  - `api/*` → API Gateway  
  - `r/*` → API Gateway  
  - `analytics/*` → API Gateway  
  - Everything else → S3  

### Infrastructure as Code
- Entire stack defined using AWS SAM  
- CloudFront behaviors, origins, and policies fully automated  
- No manual console configuration required  

---


---

# CloudFront Multi‑Origin Routing

A key part of this project is the CloudFront configuration.  
The distribution includes:

- S3 origin for static assets  
- API Gateway origin for backend APIs  
- Four cache behaviors:
  - `shorten`  
  - `api/*`  
  - `r/*`  
  - `analytics/*`  

Each behavior forwards requests to API Gateway using AWS managed policies.


This ensures:

- No caching of API responses  
- Correct forwarding of path, query string, and headers  
- Clean URLs without hardcoding API Gateway endpoints  
- Fully automated CloudFront configuration  

---

# Design Decisions and Tradeoffs

## Scalability

- Lambda functions scale automatically with demand.  
- DynamoDB provides near‑infinite horizontal scalability.  
- CloudFront caches static assets globally for low latency.  
- EventBridge decouples analytics processing from user requests.  

This architecture supports sudden traffic spikes without manual intervention.

## Cost Optimization

- Pay‑per‑use model for Lambda, API Gateway, and EventBridge.  
- DynamoDB on‑demand mode avoids over‑provisioning.  
- CloudFront reduces API Gateway invocations for static assets.  
- No servers, containers, or long‑running compute.  

The system remains extremely low‑cost even under moderate traffic.

## Security

- CloudFront Origin Access Identity (OAI) restricts S3 bucket access.  
- API Gateway provides request validation and throttling.  
- IAM policies restrict Lambda access to only required DynamoDB tables.  
- HTTPS enforced at CloudFront and API Gateway.  
- No public S3 access.  

Security is built into every layer of the architecture.

## Operational Excellence

- Fully automated deployment using AWS SAM.  
- CloudFront behaviors defined in IaC to avoid manual console drift.  
- Event‑driven analytics pipeline reduces coupling.  
- Logging and monitoring available through CloudWatch.  
- Stateless compute simplifies debugging and rollback.  

The system is designed for reliability, maintainability, and minimal operational overhead.

---

# Why I Designed It This Way

This architecture reflects real‑world cloud engineering principles:

### Scalability
The system scales automatically at every layer. Lambda, DynamoDB, CloudFront, and API Gateway all support massive concurrency without manual intervention.

### Cost Optimization
The entire system runs on pay‑per‑use services. There are no servers, no idle compute, and no over‑provisioned capacity.

### Security
CloudFront OAI, IAM least‑privilege policies, HTTPS enforcement, and API Gateway throttling ensure a secure-by-default design.

### Operational Excellence
Everything is defined in Infrastructure‑as‑Code. CloudFront behaviors, origins, and policies are fully automated, eliminating manual configuration and preventing drift.

This project demonstrates the ability to design, build, and deploy a production‑grade serverless system using modern AWS best practices.

---

# Conclusion

This repository showcases a complete, end‑to‑end serverless application with real‑time analytics, global distribution, event‑driven processing, and fully automated infrastructure. It is designed to highlight practical cloud engineering skills and architectural reasoning suitable for professional environments.



