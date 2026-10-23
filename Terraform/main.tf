terraform {
  required_version = ">= 1.0"
}

# Placeholder for provider configuration
provider "local" {}

# Example resource
resource "local_file" "example" {
  content  = "Hello Terraform!"
  filename = "${path.module}/hello.txt"
}
