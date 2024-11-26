# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MIT

terraform {
  required_providers {
    linode = {
      source = "linode/linode"
      version = "2.29.1"
    }
  }
}

provider "linode" {
  token = var.linode_token
}

resource "linode_instance" "assetsment_server" {
  label           = "assetsment"
  image           = var.image
  region          = var.location
  type            = var.type
  authorized_keys = [var.ssh_public_key]
  root_pass       = var.root_password

  tags       = ["Assetsment"]
  swap_size  = 500
  private_ip = true

  connection {
    type        = "ssh"
    user        = "root"
    password    = var.root_password
    host        = linode_instance.assetsment_server.ip_address
    private_key = var.ssh_private_key
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt update",
      "curl -fsSL https://get.docker.com -o get-docker.sh",
      "sh get-docker.sh",
      "git clone https://github.com/bramenn/thingsboard.git",
      "cd thingsboard",
      "touch .env",
      "echo 'TB_QUEUE_TYPE=rabbitmq' >> .env",
      "echo 'TB_QUEUE_RABBIT_MQ_USERNAME=bramen' >> .env",
      "echo 'TB_QUEUE_RABBIT_MQ_PASSWORD=bramen' >> .env",
      "echo 'TB_QUEUE_RABBIT_MQ_HOST=rabbitmq' >> .env",
      "echo 'TB_POSTGRESQL_URL=jdbc:postgresql://172.235.142.231:5432/thingsboard' >> .env",
      "echo 'TB_POSTGRESQL_USER=bramen' >> .env",
      "echo 'TB_POSTGRESQL_PASSWORD=bramen' >> .env",
      "echo 'TB_POSTGRESQL_DB_NAME=thingsboard' >> .env",
      "docker compose up -d"
    ]
  }
}
