# Capstone Project 🚀

## Objective

Welcome to my first azure Capstone Project! The goal of this project is to setup an infrasture for a Azure web application.


## Architectural Diagram


   ###   Diagram Details

```
Diagram details
 The Azure cloud architectural diagram displays the a web application
Components:
  - Azure Cloud
  - Azure Virtual Network: The Virtual network is a dedicated virtual network that provides isolation and security for the web application.
  - Subnets: The VPC is divided into two subnets: a public subnet and a private subnet. The public subnet is used for the load balancer and the 
  - Virtaul Machine: bastion host, while the private subnet is used for the web application and the database. The bastion host is a secure way to access the resources in the private subnet.
  - NAT Gateway: The NAT Gateway provides outbound internet access for the resources in the private subnet.
  - Load Balancer: The load balancer distributes traffic across the web servers in the private subnet.
  - Key Vault: The Key Vault is used to store the encryption key for the database.
  - SQL Database: The SQL Database is a managed relational database service that hosts the web application database.
  - SQL Database Read Replica: The SQL Database read replica provides read-only access to the database, which can be used to improve performance for read-heavy workloads.
  - App Service Plan: The App Service Plan provides the resources needed to run the web application, such as CPU, memory, and storage.
  - App Service: The App Service is a managed service that makes it easy to deploy and run web applications in the cloud.

Network Flow:

  - Users access the web application through the public IP address of the load balancer.
  - The load balancer distributes traffic across the web servers in the private subnet
  - The web servers access the database through the private IP address of the SQL Database read replica.
  - The SQL Database read replica provides read-only access to the database.
  - The web servers respond to the users' requests.

Security:

  - The VPC provides isolation and security for the web application.
  - The NAT Gateway provides outbound internet access for the resources in the private subnet, but prevents inbound traffic from reaching those resources.
  - The bastion host provides a secure way to access the resources in the private subnet.
  - The Key Vault is used to store the encryption key for the database, which helps to protect the database from unauthorized access.

```


## Approach
<details>
<summary>Step 1</summary>

- Setup Pulumi
  - Install Pulumi
  - Configure Pulumi
  - Update main file with Azure resources needed

</details>




