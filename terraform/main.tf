resource "azurerm_resource_group" "sre-challenge-flaschenpost" {
  name     = "sre-challenge-flaschenpost"
  location = var.resource_group_location

  tags = {
    department = "SRE"
  }
}

resource "azurerm_storage_account" "srechallengeflaschenpost" {
  name                     = "srechallengeflaschenpost"
  resource_group_name      = azurerm_resource_group.sre-challenge-flaschenpost.name
  location                 = var.resource_group_location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  access_tier              = "Hot"
  
  tags = {
    department = "SRE"
  }
}

resource "azurerm_storage_container" "sre" {
  name                  = "sre"
  storage_account_id    = azurerm_storage_account.srechallengeflaschenpost.id
  container_access_type = "private"
}