# Getting Started

This guide provides step-by-step instructions for getting started with the Latency-Sensitive Chemical Synthesis Optimization Engine.

## Prerequisites

* Docker installed on your system

* Kubernetes installed on your system

* Node.js and npm installed on your system

## Step 1: Clone the Repository

Clone the chemical-synthesis-optimizer repository using the following command:

```bash
 git clone https://github.com/your-username/chemical-synthesis-optimizer.git
```

## Step 2: Build the Docker Image

Build the Docker image using the following command:

```bash
 docker build -t chemical-synthesis-optimizer .
```

## Step 3: Deploy the Engine

Deploy the engine using the following command:

```bash
 kubectl apply -f deployment.yaml
```

## Step 4: Start the Engine

Start the engine using the following command:

```bash
 kubectl rollout status deployment/chemical-synthesis-optimizer
```

## Step 5: Access the Engine

Access the engine using the following command:

```bash
 kubectl port-forward deployment/chemical-synthesis-optimizer 8080:8080 &
```

You can now access the engine by visiting http://localhost:8080 in your web browser.

# Troubleshooting

If you encounter any issues during the deployment process, you can check the logs using the following command:

```bash
 kubectl logs deployment/chemical-synthesis-optimizer
```
