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

Packages: from flagger import Swagger, swag

@swag_from({
    'tags': [
        'Calculator'
    ],
    'summary': 'Calculate net pay after tax',
    'description': 'Endpoint to calculate the net pay after a 15% tax deduction from the provided salary before tax.',
    'parameters': [
        {
            'name': 'before_tax',
            'in': 'query',
            'type': 'integer',
            'required': True,
            'description': 'Salary before tax'
        }
    ],
    'responses': {
        200: {
            'description': 'Net pay after tax',
            'schema': {
                'type': 'object',
                'properties': {
                    'pay_after_tax': {
                        'type': 'number',
                        'description': 'Net pay after 15% tax deduction'
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
