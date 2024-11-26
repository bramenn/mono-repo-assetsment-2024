# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MIT

output "ip_address" {
  value = linode_instance.assetsment_server.ip_address
  description = "The public IP address of your droplet application."
}
