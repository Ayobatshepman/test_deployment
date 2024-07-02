# test_deployment

deploying a tax function

### GCP deployment path

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

# Swagger set up
```
from flasgger import Swagger, swag_from

@swag_from({
    'tags': [
        'Name'
    ],
    'summary': *'Summary of what the app does',
    'description': *'Detailed description of what the endpoint does',
    'parameters': [
        {
            'name': *'name of the input',
            'in': 'query',
            'type': *'is it interger, string, float',
            'required': *is it required or not (True or False),
            'description': *'decription of the input parameter'
        }
    ],
    'responses': {
        200: {
            'description': *'Description of the output',
            'schema': {
                'type': 'object',
                'properties': {
                    *'name of the output': {
                        'type': *'is it interger, string, float',
                        'description': *'Description of the output'
                    }
                }
            },
            'examples': {
                'application/json': {
                    'pay_after_tax': 850
                }
            }
        },
        400: {
            'description': 'Invalid input error',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string',
                        'description': 'Error message'
                    }
                }
            },
            'examples': {
                'application/json': {
                    'error': 'Invalid input. Please provide a valid integer for before_tax.'
                }
            }
        }
    }
})
```
