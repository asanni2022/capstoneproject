import pulumi
import pulumi_azure as azure
from pulumi_azure import core

# Create an Azure Resource Group
resource_group = core.ResourceGroup('rg')

# Create a virtual network
virtual_network = azure.network.VirtualNetwork('vnet',
    resource_group_name=resource_group.name,
    address_spaces=['10.0.0.0/16'])

# Create a public subnet
public_subnet = azure.network.Subnet('public-subnet',
    resource_group_name=resource_group.name,
    virtual_network_name=virtual_network.name,
    address_prefix='10.0.1.0/24')

# Create a private subnet
private_subnet = azure.network.Subnet('private-subnet',
    resource_group_name=resource_group.name,
    virtual_network_name=virtual_network.name,
    address_prefix='10.0.2.0/24')

# Create a Bastion Host
bastion_host = azure.network.BastionHost("bastion",
    resource_group_name=resource_group.name,
    location=resource_group.location,
    subnet_id=azure.network.SubnetAssociation('association',
        subnet_id=public_subnet.id,
        bastion_host=bastion_host
    ).id
)

# Create an Auto Scaling Group
autoscale_setting = azure.monitoring.AutoscaleSetting("autoscale",
    resource_group_name=resource_group.name,
    enabled=True,
    target_resource_id=virtual_network.id,
    profiles=[{
        "name": "Auto1",
        "capacity": {
            "default": "1",
            "maximum": "2",
            "minimum": "1"
        },
        "rules": [{
            "metric_trigger": {
                "metric_name": "Percentage CPU",
                "metric_resource_id": virtual_network.id,
                "time_grain": "PT1M",
                "statistic": "Average",
                "time_window": "PT5M",
                "time_aggregation": "Average",
                "operator": "GreaterThanOrEqual",
                "threshold": 75
            },
            "scale_action": {
                "direction": "Increase",
                "type": "ChangeCount",
                "value": "1",
                "cooldown": "PT1M"
            }
        }]
    }]
)

# Create Azure Service Bus
servicebus_namespace = azure.servicebus.Namespace("servicebus",
    resource_group_name=resource_group.name,
    location=resource_group.location
)

# Create Azure Application Insight
app_insight = azure.appinsights.Insights("appinsight",
    resource_group_name=resource_group.name,
    location=resource_group.location,
    application_type="web"
)

# Create Azure Key Vault
key_vault = azure.keyvault.KeyVault("keyvault",
    resource_group_name=resource_group.name,
    location=resource_group.location,
    tenant_id=azure.core.Tenant('tenant',
        display_name='Ten').id,
    sku_name="standard"
)

# Create Azure Network Security Group
network_sg = azure.network.NetworkSecurityGroup("nsg",
    resource_group_name=resource_group.name,
    location=resource_group.location,
    security_rules=[
        azure.network.NetworkSecurityGroupSecurityRuleArgs(
            name="SSH",
            priority=1001,
            direction="Inbound",
            access="Allow",
            protocol="Tcp",
            source_port_range="*",
            source_address_prefix="Internet",
            destination_port_range=[22],
            destination_address_prefix="*"
        ),
    ]
)

# Create a Postgres DB
database_account = azure.postgresql.Server('pg-server',
    resource_group_name=resource_group.name,
    location=resource_group.location,
    sku_name="B_Gen5_2",
    administrator_login="adminlogin",
    administrator_login_password="adminpassword",
    ssl_enforcement="Enabled",
    storage_mb=51200,
    version="9.5"
)

# Export the connection string for the storage account
pulumi.export('connection_string', database_account.connection_strings[0])

