# 🚀 URL Shortener DevOps Project

---

## 📌 Overview

This project demonstrates a **complete DevOps pipeline** using a URL Shortener application.

It includes:

* Application development (Flask)
* Containerization (Docker)
* Orchestration (Kubernetes - Minikube)
* CI/CD (GitHub Actions)
* Public exposure (ngrok)

---

# 🧩 Tech Stack

* Python (Flask)
* SQLite
* Docker
* Kubernetes (Minikube)
* GitHub Actions
* ngrok

---

# 📁 Project Structure

```
url-shortener-devops/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── urls.db
│
├── templates/
│   └── index.html
│
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│
└── .github/workflows/
    └── main.yml
```

---

# ⚙️ HOW TO RUN THE PROJECT

---

## 🟢 1. Run Normally (Without Docker)

### Step 1: Activate virtual environment

```
source venv/Scripts/activate
```

### Step 2: Install dependencies

```
pip install -r requirements.txt
```

### Step 3: Run app

```
python app.py
```

### Step 4: Open browser

```
http://localhost:5000
```

---

## 🐳 2. Run Using Docker

### Step 1: Build image

```
docker build -t url-shortener .
```

### Step 2: Run container

```
docker run -p 5000:5000 url-shortener
```

### Step 3: Open

```
http://localhost:5000
```

---

## ☸️ 3. Run Using Kubernetes (Minikube)

### Step 1: Start Docker Desktop

---

### Step 2: Start Minikube

```
minikube start --driver=docker
```

---

### Step 3: Go to project folder

```
cd E:\url-shortener-devops
```
kubectl get nodes
---

### Step 4: Deploy application

```
kubectl apply -f k8s/
```

---

### Step 5: Check pods

```
kubectl get pods
```

---

### Step 6: Run service

```
minikube service url-shortener-service
```

---

# 🌐 4. Make App Public (ngrok)

---

### Step 1: Run service (IMPORTANT)

```
minikube service url-shortener-service
```

You will get:

```
http://127.0.0.1:XXXXX
```

---

### Step 2: Run ngrok

```
ngrok http XXXXX
```

---

### Step 3: Open public URL

```
https://xxxxx.ngrok-free.app
```

---

# 🔄 CI/CD Pipeline

* Trigger: Git push
* Action:

  * Build Docker image
  * Push to Docker Hub

---

# 🧠 HOW SYSTEM WORKS

```
User → ngrok → Minikube → Kubernetes Service → Pods → Flask App → Database
```

---

# ⚠️ COMMON ERRORS + FIXES

---

## ❌ Error: docker not running

### Fix:

* Open Docker Desktop
* Wait until running

---

## ❌ Error: minikube not starting

### Fix:

```
minikube start --driver=docker
```

---

## ❌ Error: kubectl cannot connect

```
Unable to connect to the server
```

### Fix:

```
minikube start
```

---

## ❌ Error: pods in "Error" state

### Fix:

```
kubectl delete deployment url-shortener
kubectl delete service url-shortener-service
kubectl apply -f k8s/
```

---

## ❌ Error: ngrok not working

### Fix:

Use correct port:

```
minikube service url-shortener-service
```

Then:

```
ngrok http <port>
```

---

## ❌ Error: path k8s not found

### Fix:

Go to project folder:

```
cd E:\url-shortener-devops
```

---

# ⚠️ IMPORTANT NOTES

* Always start Docker before Minikube
* Do not close Minikube service terminal
* ngrok URL changes every time
* Project is local unless exposed via ngrok

---

# 🎯 FEATURES

* URL shortening
* Redirection
* Click tracking
* Dockerized app
* Kubernetes deployment
* Scalable architecture
* CI/CD automation

---

# 🎓 VIVA EXPLANATION (SHORT)

This project demonstrates a DevOps pipeline where:

* A Flask application is developed
* Containerized using Docker
* Deployed on Kubernetes
* Scaled using replicas
* Automated using CI/CD
* Exposed to internet using ngrok

---

# 🏁 CONCLUSION

This project shows:

* End-to-end DevOps lifecycle
* Real-world deployment practices
* Scalable system design

---

# 👨‍💻 AUTHOR

Prateek

---
