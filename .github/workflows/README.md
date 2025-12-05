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
