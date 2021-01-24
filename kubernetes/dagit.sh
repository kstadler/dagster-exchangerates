export DAGIT_POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=dagster,app.kubernetes.io/instance=dagster,component=dagit" -o jsonpath="{.items[0].metadata.name}")
echo "Visit http://127.0.0.1:8080 to open Dagit"
kubectl --namespace default port-forward $DAGIT_POD_NAME 8080:80
