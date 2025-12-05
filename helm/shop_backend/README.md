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