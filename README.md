# 🚀 DevOps Mini Project

## Scalable URL Shortener with CI/CD, Docker, Kubernetes, and Terraform

---

## 📌 Project Overview

This project demonstrates a **complete DevOps pipeline** by building and deploying a real-world **URL Shortener application**.

The system allows users to:

* Generate short URLs
* Redirect to original URLs
* Track basic usage

The project integrates modern DevOps tools for **automation, containerization, orchestration, and CI/CD**.

---

## 🧩 Tech Stack

* Backend: Python (Flask)
* Database: SQLite
* Containerization: Docker
* Orchestration: Kubernetes (Minikube)
* CI/CD: GitHub Actions
* Registry: Docker Hub

---

## 🏗️ Architecture

```
User → Flask App → Database
         ↓
      Docker
         ↓
   Docker Hub
         ↓
   Kubernetes (Minikube)
         ↓
     Scaling
```

---

## ⚙️ How to Run the Project

---

### 🔹 1. Run Locally

```bash
python app.py
```

Open:

```
http://localhost:5000
```

---

### 🔹 2. Run Using Docker

```bash
docker build -t url-shortener .
docker run -p 5000:5000 yourusername/url-shortener
```

---

### 🔹 3. Run Using Kubernetes (Minikube)

#### Start Minikube:

```powershell
& "C:\Program Files\Kubernetes\Minikube\minikube.exe" start --driver=docker
```

#### Deploy application:

```bash
kubectl apply -f k8s/
```

#### Access service:

```powershell
& "C:\Program Files\Kubernetes\Minikube\minikube.exe" service url-shortener-service
```

---

## 🔄 CI/CD Pipeline

Implemented using **GitHub Actions**.

### Workflow:

* Code pushed to GitHub
* Pipeline triggered
* Docker image built
* Image pushed to Docker Hub

---

## 🐳 Docker Commands

```bash
docker build -t yourusername/url-shortener .
docker push yourusername/url-shortener
```

---

## ☸️ Kubernetes Commands

```bash
kubectl get pods
kubectl get services
kubectl scale deployment url-shortener --replicas=4
```

---

## 🎯 Features

* URL shortening
* Redirection system
* Click tracking
* Containerized deployment
* Scalable using Kubernetes
* Automated CI/CD pipeline

---

## 🧪 Demo Steps

1. Open application
2. Enter long URL
3. Generate short URL
4. Click and verify redirection
5. Show Docker image
6. Show Kubernetes pods
7. Scale application
8. Show CI/CD pipeline

---

## 🧠 Viva Explanation

### What is DevOps?

DevOps is a combination of development and operations practices that automate software delivery.

### Why Docker?

To ensure consistent environment and portability.

### Why Kubernetes?

To manage and scale containerized applications.

### What is CI/CD?

Continuous Integration and Continuous Deployment.

### Why Minikube?

To run Kubernetes locally.

---

## 📁 Project Structure

```
url-shortener-devops/
│
├── app.py
├── models.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile / GitHub Actions
│
├── templates/
│   └── index.html
│
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│
├── terraform/
│   └── main.tf
```

---

## 🏁 Conclusion

This project demonstrates a complete DevOps lifecycle:

* Application development
* Containerization
* Continuous Integration
* Continuous Deployment
* Orchestration and scaling

---

## 👨‍💻 Author

Shetty

---
