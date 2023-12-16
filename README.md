# vagrant-spark-ansible-k8s

cp ./spark/* to master_nodes
kubectl create namespace spark
kubectl apply -f spark-master-service.yaml -n spark
kubectl apply -f spark-deployment.yaml -n spark