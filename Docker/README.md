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
