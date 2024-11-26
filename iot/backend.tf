terraform {
  backend "remote" {
    hostname = "app.terraform.io"
    organization = "bramen"

    workspaces {
      name = "assetsment"
    }
  }
}
