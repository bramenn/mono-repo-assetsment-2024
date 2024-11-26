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
  token = "64d083e53f5257d8bcc153f2e09afafe60d527b320e4fa40da44fc64bccea9e1"
}

resource "linode_instance" "assetsment_server" {
  label           = "assetsment"
  image           = "linode/debian12"
  region          = "us-mia"
  type            = "g6-standard-2"
  root_pass       = "H3lSt@n1225"

  tags       = ["Assetsment"]
  swap_size  = 500
  private_ip = true

  connection {
    type        = "ssh"
    user        = "root"
    password    = "H3lSt@n1225"
    host        = linode_instance.assetsment_server.ip_address
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
      "echo 'TB_QUEUE_RABBIT_MQ_HOST=172.235.142.231' >> .env",
      "echo 'SPRING_DATASOURCE_URL=jdbc:postgresql://172.235.142.231:5432/thingsboard' >> .env",
      "echo 'SPRING_DATASOURCE_USERNAME=bramen' >> .env",
      "echo 'SPRING_DATASOURCE_PASSWORD=bramen' >> .env",
      "docker compose up -d"
    ]
  }
}
