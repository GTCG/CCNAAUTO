terraform {
  required_providers {
    iosxe = {
      source  = "CiscoDevNet/iosxe"
      version = ">= 0.5.0"
    }
  }
}

variable "device_username" { default = "admin" }
variable "device_password" { default = "admin" }

provider "iosxe" {
  username = var.device_username
  password = var.device_password
  host     = "192.168.110.82"
  insecure = true   # self-signed cert in the lab
}

resource "iosxe_interface_loopback" "lo100" {
  name              = 100
  description       = "Created by Terraform"
  ipv4_address      = "192.0.2.100"
  ipv4_address_mask = "255.255.255.255"
}
resource "iosxe_interface_loopback" "lo101" {
 name			= 204
 description		= "created by me"
 ipv4_address		= "192.168.100.204"
 ipv4_address_mask	= "255.255.255.0"
}
