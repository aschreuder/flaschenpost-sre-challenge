## Project Structure
Each challenge is isolated in its own folder and contains a dedicated README file, as can be seen in the below structure.

### Tree structure

```
.
├── backstage
│   ├── README.md
│   └── template.yaml
├── Docker
│   ├── Dockerfile
│   └── README.md
├── FlaskApp
│   ├── app.py
│   ├── README.md
│   └── requirements.txt
├── helm
│   └── shop_backend
│       ├── Chart.yaml
│       ├── README.md
│       ├── templates
│       │   ├── _helpers.tpl
│       │   ├── configmap.yaml
│       │   ├── cronjob.yaml
│       │   ├── deployment.yaml
│       │   ├── hpa.yaml
│       │   ├── ingress.yaml
│       │   ├── secret.yaml
│       │   ├── service.yaml
│       │   └── tests
│       │       └── test-connection.yaml
│       ├── values-dev.yaml
│       ├── values-prod.yaml
│       ├── values-stg.yaml
│       ├── values.schema.json
│       └── values.yaml
├── README.md
└── terraform
    ├── main.tf
    ├── outputs.tf
    ├── provider.tf
    ├── README.md
    ├── tfplan.txt
    ├── variables.tf
    └── vars
        └── dev.tfvars
```