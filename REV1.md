python app.py






docker build -t url-shortener .

docker images

docker run -p 5000:5000 url-shortener




minikube start --driver=docker

kubectl apply -f k8s/

kubectl get pods

kubectl get services

minikube service url-shortener-service

kubectl scale deployment url-shortener --replicas=3


ngrok http <port>



PUSH FOR CI/CD TRIGGER