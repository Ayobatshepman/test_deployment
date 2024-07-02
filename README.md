# test_deployment

deploying a tax function

## GCP deployment path

1. first authenticate with docker: [gcloud auth configure-docker us-central1-docker.pkg.dev]
2. [docker build -t us-central1-docker.pkg.dev/ayoba-183a7/gcf-artifacts/image-name:tag .]
3. [docker push us-central1-docker.pkg.dev/ayoba-183a7/gcf-artifacts/image-name:tag]
4. Apply the Deployment configuration:
   - [kubectl apply -f deployment.yaml] 
   - [kubectl apply -f service.yaml] 
   - Auth kubernetes cluster: [gcloud container clusters get-credentials us-central1-ayoba-composer-4bf99150-gke --region us-central1 --project ayoba-183a7] 
5. Check the status of your Pods
   - [kubectl get pods]
   - [kubectl get services]
