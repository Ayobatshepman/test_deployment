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
        'TagName'  # Replace with the name of the tag, e.g., 'User'
    ],
    'summary': 'Summary of what the app does',  # Provide a brief summary of the endpoint
    'description': 'Detailed description of what the endpoint does',  # Provide a detailed description of the endpoint
    'parameters': [
        {
            'name': 'input_name',  # Replace with the name of the input parameter, e.g., 'user_id'
            'in': 'query',  # Specify where the parameter is located (query, path, body, header)
            'type': 'type',  # Specify the type of the parameter (integer, string, float)
            'required': True,  # Specify if the parameter is required (True or False)
            'description': 'Description of the input parameter'  # Provide a description of the input parameter
        }
    ],
    'responses': {
        200: {
            'description': 'Description of the output',  # Provide a description of the successful output
            'schema': {
                'type': 'object',
                'properties': {
                    'output_name': {  # Replace with the name of the output field, e.g., 'user_name'
                        'type': 'type',  # Specify the type of the output field (integer, string, float)
                        'description': 'Description of the output'  # Provide a description of the output field
                    }
                }
            },
            'examples': {
                'application/json': {
                    'example_field': 'example_value'  # Replace with an example of the JSON response
                }
            }
        },
        400: {
            'description': 'Invalid input error',  # Description of the 400 error response
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string',
                        'description': 'Error message'  # Description of the error message
                    }
                }
            },
            'examples': {
                'application/json': {
                    'error': 'Invalid input. Please provide a valid input.'  # Example error message
                }
            }
        }
    }
})
def your_endpoint_function():
    # Your endpoint implementation
    pass

```
