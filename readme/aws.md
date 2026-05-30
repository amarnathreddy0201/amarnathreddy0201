# AI Engineer Interview Preparation Guide
## Quick Revision Notes (2–3 Lines Per Topic)

---

# AWS

## EC2
AWS EC2 provides virtual machines for running applications, AI models, and training jobs. It offers full control over infrastructure, operating systems, and GPU configurations but requires manual management and scaling.

## SageMaker
Amazon SageMaker is a fully managed machine learning platform that simplifies model training, deployment, and monitoring. It reduces operational overhead and accelerates ML development.

## ECS
Elastic Container Service (ECS) is AWS's container orchestration service for deploying and managing Docker containers. It is simpler than Kubernetes and integrates well with AWS services.

## EKS
Elastic Kubernetes Service (EKS) is a managed Kubernetes platform on AWS. It provides advanced orchestration, scalability, and portability for large-scale AI applications.

## S3
Amazon S3 is object storage used for storing datasets, model artifacts, logs, images, and backups. It is highly durable, scalable, and cost-effective.

## CloudWatch
CloudWatch is AWS's monitoring and observability service. It tracks metrics, logs, latency, CPU/GPU utilization, and application performance.

## IAM
Identity and Access Management (IAM) controls who can access AWS resources. It follows the principle of least privilege, granting only necessary permissions.

---

# Optimization

## Quantization
Quantization reduces model precision from FP32/FP16 to INT8 or INT4. This lowers memory usage, improves inference speed, and reduces infrastructure costs with minimal accuracy loss.

## Distillation
Knowledge Distillation transfers knowledge from a large teacher model to a smaller student model. The resulting model is faster, cheaper, and easier to deploy while retaining most capabilities.

## Request Batching
Batching combines multiple requests into a single GPU execution. It improves throughput and GPU utilization by processing requests more efficiently.

## TensorRT
TensorRT is NVIDIA's inference optimization framework. It accelerates deep learning models by optimizing computation graphs and reducing inference latency.

## Caching
Caching stores frequently accessed data in memory to avoid repeated computation. It improves response times, reduces costs, and increases scalability.

---

# Latency

## Latency
Latency is the total time taken to process a request and return a response. Lower latency improves user experience and application responsiveness.

## P50 Latency
P50 represents the median response time of requests. It shows the typical performance experienced by users.

## P95 Latency
P95 indicates the response time within which 95% of requests are completed. It is one of the most important production performance metrics.

## P99 Latency
P99 measures the response time for 99% of requests. It helps identify extreme slowdowns and performance bottlenecks.

## Cold Start
A cold start occurs when a new container, function, or server initializes before handling requests. This initialization time can temporarily increase latency.

---

# Scalability

## Scalability
Scalability is the ability of a system to handle increasing workloads without performance degradation. It ensures reliability during traffic growth.

## Vertical Scaling
Vertical scaling increases the resources of an existing machine, such as CPU, RAM, or GPU capacity. It is simple but limited by hardware constraints.

## Horizontal Scaling
Horizontal scaling adds more servers or containers to distribute workload. It provides better fault tolerance and virtually unlimited growth.

## Load Balancer
A load balancer distributes incoming traffic across multiple servers. This prevents overload and improves system availability.

## Autoscaling
Autoscaling automatically adds or removes resources based on workload metrics like CPU, GPU, latency, or queue length. It balances performance and cost.

---

# Security

## Encryption at Rest
Encryption at rest protects stored data such as files, databases, and backups. AWS KMS is commonly used to manage encryption keys.

## Encryption in Transit
Encryption in transit protects data while moving between systems using secure protocols such as HTTPS and TLS. It prevents unauthorized interception.

## Secrets Manager
AWS Secrets Manager securely stores sensitive credentials like API keys and passwords. It eliminates the need to hardcode secrets in applications.

## Prompt Injection
Prompt injection is an attack where users manipulate prompts to override system instructions. Mitigation techniques include validation, isolation, and output filtering.

## PII Protection
Personally Identifiable Information (PII) includes sensitive user data such as emails, phone numbers, and IDs. Protection methods include encryption, masking, and tokenization.

---

# RAG (Retrieval-Augmented Generation)

## RAG
RAG combines document retrieval with language model generation. It improves answer accuracy by providing relevant context before generating responses.

## Embeddings
Embeddings are numerical vector representations of data that capture semantic meaning. They are used for similarity search and retrieval systems.

## Vector Database
A vector database stores embeddings and performs similarity searches efficiently. Examples include Pinecone, Milvus, Weaviate, and pgvector.

## ANN Search
Approximate Nearest Neighbor (ANN) search finds similar vectors quickly without performing exact comparisons. It enables scalable semantic search.

## Retriever
The retriever identifies the most relevant documents from a vector database based on a user's query. These documents are passed to the LLM as context.

---

# MLOps

## Model Drift
Model drift occurs when production data changes over time, causing model performance to degrade. Continuous monitoring and retraining help mitigate drift.

## Data Drift
Data drift happens when the distribution of incoming data differs from training data. It can reduce prediction accuracy.

## Concept Drift
Concept drift occurs when the relationship between inputs and outputs changes. Models may need retraining to adapt to new patterns.

## Blue-Green Deployment
Blue-Green deployment maintains two environments: one active and one updated version. It enables safe deployments with quick rollback options.

## Canary Deployment
Canary deployment gradually releases a new version to a small percentage of users before full rollout. This minimizes deployment risk.

---

# Advanced AI Infrastructure

## vLLM
vLLM is a high-performance LLM serving framework that improves throughput and GPU efficiency. It uses PagedAttention for optimized KV cache management.

## KV Cache
KV Cache stores previous transformer computations during token generation. This avoids redundant calculations and significantly reduces latency.

## GPU Utilization
GPU utilization measures how effectively GPU resources are used. Higher utilization generally results in better throughput and lower infrastructure costs.

## Throughput
Throughput is the number of requests a system can process per second. High throughput is essential for serving large numbers of users efficiently.

## Observability
Observability is the ability to understand system behavior using logs, metrics, and traces. It helps engineers monitor, debug, and optimize AI systems.

---

# System Design

## API Gateway
An API Gateway acts as the entry point for client requests. It handles routing, authentication, throttling, and request management.

## Redis
Redis is an in-memory data store commonly used for caching, session storage, and rate limiting. It significantly reduces response times.

## Queue System
Message queues such as SQS or Kafka enable asynchronous processing. They improve reliability and help handle traffic spikes.

## Microservices
Microservices divide applications into smaller independent services. This improves scalability, maintainability, and deployment flexibility.

## Monitoring
Monitoring tracks infrastructure, application, and model performance metrics. It helps detect issues before they impact users.

---

# Behavioral Concepts

## Performance Optimization
Performance optimization focuses on reducing latency, improving throughput, and lowering infrastructure costs. It often involves profiling and eliminating bottlenecks.

## Cost Optimization
Cost optimization aims to reduce cloud spending while maintaining performance. Techniques include quantization, autoscaling, caching, and spot instances.

## Root Cause Analysis
Root Cause Analysis (RCA) identifies the underlying cause of a problem rather than just addressing symptoms. It is essential for reliable production systems.

## Reliability
Reliability ensures a system consistently performs its intended function. Techniques include redundancy, failover mechanisms, and health monitoring.

## Fault Tolerance
Fault tolerance enables systems to continue operating even when components fail. It is achieved through replication, backups, and distributed architectures.

---
# Interview Success Formula

For every system design or production question, answer in this format:

1. Problem
2. Root Cause
3. Solution
4. Tradeoffs
5. Impact

This structure demonstrates strong engineering thinking and is highly valued in AI Engineer interviews.