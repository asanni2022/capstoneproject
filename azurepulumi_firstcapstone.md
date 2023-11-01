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

## Infrastructure Code

```
import pulumi
import pulumi_azure as azure

# Create an Azure Resource Group
resource_group = azure.core.ResourceGroup("my-resource-group")

# Create an Azure Virtual Network (VPC)
vpc = azure.network.VirtualNetwork("my-vpc",
    resource_group_name=resource_group.name,
    address_spaces=["10.0.0.0/16"],
    location="eastus2")

# Create an Azure Subnet for the public subnet
public_subnet = azure.network.Subnet("my-public-subnet",
    resource_group_name=resource_group.name,
    virtual_network_name=vpc.name,
    address_prefix="10.0.0.0/24")

# Create an Azure Subnet for the private subnet
private_subnet = azure.network.Subnet("my-private-subnet",
    resource_group_name=resource_group.name,
    virtual_network_name=vpc.name,
    address_prefix="10.1.0.0/24")

# Create an Azure NAT Gateway
nat_gateway = azure.network.NatGateway("my-nat-gateway",
    resource_group_name=resource_group.name,
    location="eastus2",
    public_ip_address=azure.network.PublicIPAddress("my-public-ip",
        resource_group_name=resource_group.name,
        allocation="Dynamic"),
)

# Create an Azure Bastion Host
bastion_host = azure.compute.BastionHost("my-bastion-host",
    resource_group_name=resource_group.name,
    virtual_network_name=vpc.name,
    ip_configurations=[azure.compute.BastionHostIPConfigurationArgs(
        name="bastion-config",
        subnet_id=public_subnet.id,
    )],
)

# Create an Azure Load Balancer
load_balancer = azure.lb.LoadBalancer("my-load-balancer",
    resource_group_name=resource_group.name,
    frontend_ip_configurations=[azure.lb.FrontendIPConfigurationArgs(
        name="public",
        public_ip_address_id=nat_gateway.public_ip_addresses[0].id,
    )],
    backend_address_pools=[azure.lb.BackendAddressPoolArgs(
        name="private",
    )],
)

# Create an Azure Key Vault
key_vault = azure.keyvault.Vault("my-key-vault",
    resource_group_name=resource_group.name,
    location="eastus2",
    sku=azure.keyvault.SkuArgs(
        name="standard",
        family="A",
        tier="2",
    ),
)

# Create an Azure Key Vault Key
key_vault_key = azure.keyvault.Key("my-key-vault-key",
    resource_group_name=resource_group.name,
    vault_uri=key_vault.vault_uri,
    key_type="RSA",
    key_size=2048,
)

# Create an Azure SQL Database
sql_database = azure.sql.Database("my-sql-database",
    resource_group_name=resource_group.name,
    location="eastus2",
    server_name="my-sql-server",
    requested_service_objective_name="S1",
    collation="SQL_Latin1_General_CP1_CI_AS",
    max_size_bytes=1073741824,  # 1 GB
    create_mode="Default",
)

# Create an Azure SQL Database read replica
sql_database_read_replica = azure.sql.Database("my-sql-database-read-replica",
    resource_group_name=resource_group.name,
    location="westus2",
    server_name="my-sql-server",
    requested_service_objective_name="S1",
    source_database_id=sql_database.id,
)

# Create an Azure SQL Database firewall rule
sql_database_firewall_rule = azure.sql.FirewallRule("my-sql-database-firewall-rule",
    resource_group_name=resource_group.name,
    server_name="my-sql-server",
    start_ip_address="0.0.0.0",
    end_ip_address="0.0.0.0",
)

# Create an Azure App Service Plan
app_service_plan = azure.appservice.Plan("my-app-service-plan",
    resource_group_name=resource_group.name,
    location="eastus2",
    sku=azure.appservice.PlanSkuArgs(
        tier="Standard",
        size="S1",
    ),
)

# Create an Azure App Service
app_service = azure.appservice.AppService("my-app-service",
    resource_group_name=resource_group.name,
    location="eastus2",
    app_service_plan_id=app_service_plan.id,
    site_config=azure.appservice.AppServiceSiteConfigArgs(
        always_on=True,
    ),
)

# Export necessary resource information
pulumi.export("bastion_host", bastion_host.fqdn)
pulumi.export("load_balancer_frontend_ip", load_balancer.frontend_ip_configurations[0].public_ip_address.id)

```




