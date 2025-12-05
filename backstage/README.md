## Backstage Deployment
The backstage software template file `template.yaml` assists developers with deploying Terraform changes while maintaining the GitOps workflow for code review principles.

### Template Structure
The custom infrastructure template renders a frontend with form inputs for project information and Azure resource categories. There are default values as well as alternative options under `enumNames` which shows available resource options. An `Advanced Options` input is included for less frequent resource types.

### Workflow
The Terraform files are fetched from the GitHub Repository, followed by `terraform init`, `terraform plan` to view changes, and `terraform show` for a summarized view. An output job confirms the generation of Terraform files and provides next steps.
