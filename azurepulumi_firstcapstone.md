# Capstone Project 🚀

## Objective

Welcome to my first azure Capstone Project! The goal of this project is to setup an infrastructure for a Azure web application.

## Architectural Diagram



![AzWebAppdeployment02Nov23](https://github.com/asanni2022/capstoneproject/assets/104282577/191c150e-1df4-481e-9cc1-d322cefbb55c)


   ###   Diagram Details


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


## Approach
<details>
<summary>Steps</summary>

  - Infrastructure breakdown
  - Setup Pulumi
  - Install Pulumi
  - Configure Pulumi
  - Update main file with Azure resources needed

</details>

Below is a detailed documentation of the Azure resources and their features to ensure the client web application is secure, scalable, available and robust. 

### Service Features:
<details>
<summary>Service Features</summary>
- **Azure Virtual Network (VPC):** Provides isolated and secure network environments in Azure. Features include custom IP addressing, routing, and network peering.

- **Azure Availability Zone:** Ensures high availability and fault tolerance by replicating applications and data across multiple data centers within an Azure region.

- **Azure Bastion Host:** Offers secure and seamless RDP and SSH access to Azure VMs over SSL. It simplifies management and enhances security.

- **Azure NAT Gateway:** Enables outbound internet access for resources in a private subnet, enhancing security by not exposing internal IPs.

- **Azure Key Vault:** Provides secure storage and management of cryptographic keys, secrets, and certificates. Offers integration with other Azure services.

- **Azure SQL Database:** A fully managed database service with features for scaling, high availability, and automated backups.

- **Azure Service Bus:** A messaging service that enables reliable and scalable communication between distributed applications.

- **Azure Application Insights:** Provides application performance and availability monitoring, including deep insights into application behavior.

- **Azure Network Security Group (NSG):** Acts as a virtual firewall to control inbound and outbound traffic. It enhances security and access control.
</details>

### Scalability and Performance:
<details>
<summary>Scalability and Performance</summary>
- **Azure Virtual Network:** Supports scaling by enabling the addition of subnets and adjusting IP address spaces. Load balancers can distribute traffic for performance.

- **Azure Availability Zone:** Enhances performance and availability by distributing workloads across multiple data centers in a region.

- **Azure Bastion Host:** Offers scalability with consistent and secure RDP/SSH access to VMs, reducing management overhead.

- **Azure NAT Gateway:** Scales with increased outbound traffic demands, ensuring network performance.

- **Azure SQL Database:** Provides options for auto-scaling, enabling automatic adjustments to performance tiers based on demand.

- **Azure Service Bus:** Scales to accommodate message volumes, supporting high throughput and reliability.

- **Azure Application Insights:** Offers performance metrics and deep insights into application performance, helping with optimization.
</details>


### Reliability and Availability:
<details>
<summary>Reliability and Availability</summary>
- **Azure Virtual Network:** Provides high reliability with built-in redundancy, and availability zones enhance fault tolerance.

- **Azure Availability Zone:** Ensures high availability by replicating resources across multiple data centers.

- **Azure Bastion Host:** Enhances security and reliability by providing secure RDP and SSH access to VMs.

- **Azure NAT Gateway:** Provides reliability for outbound traffic, with redundancy and fault tolerance mechanisms.

- **Azure SQL Database:** Offers high availability with automated backups and geo-replication.

- **Azure Service Bus:** Ensures message reliability with built-in redundancy and failover.

- **Azure Application Insights:** Monitors application availability and performance, helping maintain high uptime.
</details>

### Security and Compliance:
<details>
<summary>Security and Compliance</summary>
- **Azure Virtual Network:** Supports network security with Network Security Groups (NSGs) and integrates with Azure Active Directory for authentication.

- **Azure Bastion Host:** Ensures secure remote access with SSL encryption and Azure Active Directory authentication.

- **Azure Key Vault:** Provides strong security for key management, secrets, and certificates, along with compliance certifications.

- **Azure SQL Database:** Offers built-in security features, including encryption, firewall rules, and role-based access control.

- **Azure Service Bus:** Supports data encryption in transit and at rest, and offers role-based access control.

- **Azure Network Security Group (NSG):** Enhances security with granular access control and network-level security rules.
</details>

### Data Storage and Management:
<details>
<summary>Data Storage and Management</summary>
- **Azure SQL Database:** Offers secure and managed relational database storage with various tiers for different storage needs.

- **Azure Key Vault:** Provides secure storage for cryptographic keys, secrets, and certificates.
</details>

### Integration Capabilities:
<details>
<summary>Integration Capabilities</summary>
- **Azure Virtual Network:** Seamlessly integrates with Azure services, and Azure Bastion Host provides secure access.

- **Azure Key Vault:** Integrates with various Azure services for secure key management and storage.

- **Azure SQL Database:** Easily integrates with other Azure services and provides connectivity options.

- **Azure Service Bus:** Seamlessly works with various Azure services for messaging and event-driven applications.

- **Azure Application Insights:** Integrates with Azure services for monitoring and diagnostics.
</details>

### Cost and Pricing Model:
<details>
<summary>Cost and Pricing Model</summary>
- Costs for Azure resources vary based on factors like usage, performance tiers, and regional availability. Refer to the Azure Pricing Calculator for detailed cost estimates.
</details>

### Management and Monitoring:
<details>
<summary>Management and Monitoring</summary>
- **Azure Bastion Host:** Provides integration with Azure Monitor for monitoring and diagnostics.

- **Azure Application Insights:** Offers extensive monitoring capabilities, including application performance, diagnostics, and alerts.
</details>

### Service-Level Agreements (SLAs):
<details>
<summary>Service-Level Agreements (SLAs)</summary>
- Azure provides SLAs for uptime, availability, performance, and support for various services. SLA details can be found on the Azure Service Level Agreements page.
</details>


## References
<details>
<summary>References</summary>
https://azure.microsoft.com/en-us/pricing/details/azure-sql-database/single/

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




