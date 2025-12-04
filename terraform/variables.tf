variable "resource_group_location" {
  type        = string
  default     = "westeurope"
  description = "Location of the resource group."
}

variable "account_tier" {
  type = string
  description = "The storage account tier"
}

variable "account_replication_type" {
  type = string
}

variable "access_tier" {
  type = string
}

variable "container_access_type" {
  type        = string
  description = "Access type for the storage container"
  default     = "private"
}
