## Terraform Infrastructure
The `hashicorp/azurerm` provider is used to provision the infrastructure in Azure. For this exercise I went with normal resource blocks instead of modules due to the simplicity of the infrastructure, however modules are always preferred in production ready environments. 

The `variables.tf` file contains certain variables which helps us to have clean code with minimal hardcoded values and ensures reusability across teams. I've also added a `dev.tfvars` file where values are defined, although this is overspec for this project, it is always best-practice to use var files. It is important to reference this file when running `terraform plan` and `terraform apply`.

### Testing Terraform locally
- `cd terraform/`
- `terraform fmt` - Optional, but good for clean Terraform code format
- `terraform init` - Initializes Terraform locally
- `terraform plan -var-file=vars/dev.tfvars -out=tfoutput.txt` - Runs Terraform plan to an output file

## Backstage Deployment
The backstage software template file `template.yaml` assists developers with deploying Terraform changes while maintaining the GitOps workflow for code review principles.

### Template Structure
The custom infrastructure template renders a frontend with form inputs for project information and Azure resource categories. There are default values as well as alternative options under `enumNames` which shows available resource options. An `Advanced Options` input is included for less frequent resource types.

### Workflow
The Terraform files are fetched from the GitHub Repository, followed by `terraform init`, `terraform plan` to view changes, and `terraform show` for a summarized view. An output job confirms the generation of Terraform files and provides next steps.

## Helm Chart Development
This Helm chart is designed to support multi-environment and multi-deployment scenarios. It provides a consistent deployment model that multiple teams can adopt while following standardized, industry best practices.

### Environment configuration
The files `values-dev.yaml`, `values-stg.yaml`, and `values-prod.yaml` define environment-specific overrides, such as:

- Resource requests and limits  
- Replica counts  
- Environment-tailored configuration values  
- Any settings that differ between dev, staging, and production  

The default `values.yaml` defines the baseline configuration shared across all environments. This ensures consistent behavior across deployments and helps prevent configuration drift.

Values inheritance follows standard Helm behavior:
`helm upgrade --install <release> . -f values-stg.yaml`
Environment-specific values override defaults in `values.yaml`.

### Deployment Flexibility

This chart supports flexible deployment patterns through conditionals such as:
`{{- if and .Values.<flag>.enabled }}`.
These allow optional components or functionality to be toggled on or off. Templates are structured to avoid hard-coded values, relying instead on configurable values from the values files. Each Kubernetes resource is defined in its own file within the templates/ directory, following Helm best practices.

### Internal vs External services
You can configure services as either internal or external by adjusting their type:

- service.type: ClusterIP - Internal service
- service.type: LoadBalancer - External service

In this project, the staging and production environments are external-facing, while development remains internal.

## Dockerfile
The Dockerfile is based on `sreflaschenpost/flaschenpost-sre-challenge:latest` and is designed for secure deployment with easy extensibility.

### Security Features

- Non-root user: Creates a dedicated non-root user (`appuser`) to enforce least-privilege best practices, assuming the base image doesn't already handle this
- Port exposure: Exposes port 80 for HTTP traffic
- Ownership management: Ensures the working directory has proper permissions for the non-root user

### Structure

- Working directory: Set to `/app` for consistent file organization
- Commented sections: Includes placeholder comments for future customization:
  - `COPY` command for adding custom application files
  - `CMD` and `ENTRYPOINT` for custom startup commands if needed

### Building and testing the image locally
- `docker build -t name:version .`
- `docker run -p 8080:80 name:version`
- `curl http://localhost:8080/`

### Notes

- The `CMD` and `ENTRYPOINT` are commented out to use the base image defaults
- Kubernetes deployment configurations (replicas, probes, HPA) are managed via Helm chart
- Environment-specific settings should be configured through Helm values

## CI/CD
This pipeline automates the build and deployment of the `shop_backend` service across multiple environments using Docker, Helm, and Kubernetes.

### Multi-Environment Deployment

The pipeline uses a matrix strategy to deploy across three environments in parallel:
- `dev` (Development)
- `stg` (Staging)  
- `prod` (Production)

Each environment is deployed to its own Kubernetes namespace, determined by `K8S_NAMESPACE: ${{ matrix.environment }}`, ensuring complete isolation between environments.

## Pipeline Stages

- Build - Builds and pushes Docker image tagged with Git commit SHA to the container registry
- Package - Installs kubectl/Helm, validates and packages the Helm chart
- Deploy - Deploys to Kubernetes using environment-specific values files (`values-{environment}.yaml`)
- Verify - Monitors rollout status and confirms pods are running successfully
- Rollback - Automatically reverts to previous release if deployment fails

### Required GitHub Secrets

The pipeline requires the following secrets to be configured in GitHub:

- `REGISTRY_URL` - Container registry URL
- `REGISTRY_USERNAME` - Registry authentication username
- `REGISTRY_PASSWORD` - Registry authentication password
- `KUBE_CONFIG` - Base64-encoded Kubernetes configuration file for cluster access

Configure in: `Settings > Secrets and variables > Actions`

## Triggering the Pipeline

The pipeline runs automatically on every push to the `main` branch, deploying to all three environments simultaneously.

### Environment-Specific Configuration

Each environment uses its own values file:
- `helm/shop_backend/values-dev.yaml`
- `helm/shop_backend/values-stg.yaml`
- `helm/shop_backend/values-prod.yaml`

These files should contain environment-specific settings such as replica counts, resource limits, and HPA configurations.

## FastAPI Application
The Python script runs a FastAPI server with 2 GET endpoints - `/movies` (which accepts a substring search parameter) and `/` (health check endpoint for testing API connectivity).

### How it works
When the `/movies` endpoint is called with a substring, it queries `https://jsonmock.hackerrank.com/api/movies/search/?Title=substr` and returns sorted movie titles as an array. The script uses `asyncio` for concurrent page fetching to optimize performance.

### Error handling
- Timeout values prevent hanging requests
- `raise HTTPException` catches HTTP errors
- Returns `None` on certain failures to prevent script breakage
- Validates that `substr` is not empty

### Running locally
- `cd FlaskApp`
- `pip install -r requirements.txt`
- `uvicorn app:app --reload` or `python app.py`
- Test the API: `curl "http://localhost:8000/movies?substr=spider"`
