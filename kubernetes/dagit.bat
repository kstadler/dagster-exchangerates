echo off
kubectl get pods --namespace default -l "app.kubernetes.io/name=dagster,app.kubernetes.io/instance=dagster-exchangerates,component=dagit" -o jsonpath="{.items[0].metadata.name}" > dagit_pod_name.txt
set /p pod=<dagit_pod_name.txt
echo "Visit http://127.0.0.1:8080 to open Dagit"
kubectl --namespace default port-forward %pod% 8080:80
