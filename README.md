# Capstone Project 🚀

Welcome to the Capstone Project! This is your unique opportunity to combine the knowledge and skills you've acquired thus far and apply them to a tangible project. This project is your canvas. While the endeavor should stretch your abilities, it must remain feasible. This collaborative journey will not only refine your skills but also provide a meaningful capstone to your learning experience.

## Daily Plan

Daily, you can expect a brief conversation and demo on a Pulumi topic. The projects listed below are optional only if you need additional practice. The remaining time we’ll allow to work on your project.

<details>
<summary>Session 1</summary>

- Introductions
  - Introduction to Infrastructure as Code
  - Describe the project and expectations
  - Describe the diagram of AWS architecture
  - Describe the tools: Python, Pulumi, GitHub, Draw.io

</details>

<details>
<summary>Session 2</summary>

- **Lecture**: Introduction to Pulumi
- **Demo**: Deploying a simple web app using Pulumi on Azure
- **Project**: Deploy a simple web app using Pulumi on Azure

</details>

<details>
<summary>Session 3</summary>

- **Lecture**: Introduction to Azure resources
- **Demo**: Deploying a virtual machine and storage using Pulumi on Azure.
- **Project**: Deploy a virtual machine and storage using Pulumi on Azure

</details>

<details>
<summary>Session 4</summary>

- **Lecture**: Deploying a data lake using Pulumi on Azure
- **Demo**: Deploying a simple data lake using Azure Blob Storage and Azure Data Lake Analytics using Pulumi on Azure
- **Project**: Deploy a simple data lake using Azure Blob Storage and Azure Data Lake Analytics using Pulumi on Azure

</details>

<details>
<summary>Session 5</summary>

- **Lecture**: Deploying a serverless function using Pulumi on Azure
- **Demo**: Deploying a simple HTTP serverless function using Pulumi on Azure
- **Project**: Deploy a simple HTTP serverless function using Pulumi on Azure

</details>

<details>
<summary>Session 6</summary>

- **Lecture**: Deploying a multi-tier web application using Pulumi on Azure
- **Demo**: Deploying a multi-tier web application using:
    - Azure App Service
    - Azure Database for PostgreSQL
    - Azure Cache for Redis
- **Project**: Deploy a multi-tier web application

</details>

<details>
<summary>Session 7</summary>

- **Lecture**: Creating a CI/CD pipeline using Azure DevOps and Pulumi
- **Demo**: Creating a CI/CD pipeline using Azure DevOps and Pulumi to deploy a simple web app to Azure
- **Project**: Create a CI/CD pipeline using Azure DevOps and Pulumi to deploy a simple web app to Azure

</details>

<details>
<summary>Session 8</summary>

- **Lecture**: Deploying a machine learning model using Pulumi on Azure
- **Demo**: Deploying a simple machine learning model to Azure Machine Learning Service using Pulumi on Azure
- **Project**: Deploy a simple machine learning model to Azure Machine Learning Service using Pulumi on Azure

</details>

<details>
<summary>Session 9</summary>

- **Lecture**: Capstone project
- **Demo**: None
- **Project**: Complete the capstone project

</details>

<details>
<summary>Session 10</summary>

- **Lecture**: Capstone project
- **Demo**: None
- **Project**: Complete the capstone project

</details>

## Capstone Project

<details>
<summary>Scenario</summary>

**Introduction:**

EgozNaSilo, a popular online shopping platform, sees a surge in user traffic during festive seasons. During these times, thousands of users actively explore products and finalize purchases. Underpinning their system is a PostgreSQL Aurora database.

**Problem Statement:**

As the festive season rolls in, the EgozNaSilo technical team identifies a recurring issue. The database finds it challenging to manage the sudden increase in read requests. This limitation hinders the application's response time, resulting in unsatisfactory user experiences. A deep dive into the system reveals that most of the application's operations are read-based. These include tasks like searching for products, providing product recommendations, and displaying reviews.

**Solution Approach:**

To circumvent this bottleneck, the team brainstormed and implemented a read replica for their Postgres Aurora database. The read replica is set up to mirror data from the primary database in real time. This ensures the replica remains current with the latest data. The primary objective is to distribute the read traffic. By diverting the read operations to the read replicas, the main database can prioritize write operations, like order processing and inventory updates.

**Outcome:**

Post-implementation of the read replica, EgozNaSilo's platform exhibits enhanced performance and swift responsiveness. The read replicas adeptly manage the intense read operations, ensuring the main database isn't overwhelmed. This strategic deployment ensures the system remains scalable, especially during high-demand periods. As a result, users enjoy a smooth and efficient shopping experience, leading to heightened customer satisfaction.

**Your Task:**

Given the reference architecture provided, your objective is to implement a similar solution but within the Azure cloud environment. Please make sure that you consider Azure's best practices for database replication and load distribution. Your goal is to create a robust and scalable system that can handle intense read operations without compromising performance.

</details>

<details>
<summary>Reference Architecture</summary>

![Reference Architecture](https://github.com/xjbar/capstone/raw/main/Screenshot%202023-10-30%20083841.png)

</details>


<details>
<summary>Architecture Details</summary>

The system deploys a robust and resilient Virtual Private Cloud (VPC) architecture, ensuring high availability by spanning across two distinct Availability Zones.

- **Virtual Private Cloud (VPC)**
  - This environment sets up a dedicated virtual network on AWS. It meticulously adheres to AWS best practices and is demarcated into both public and private subnets.
  - **Public Subnets**
    - **Managed NAT Gateways:** These gateways are integral to facilitate outbound internet access for resources nestled within the private subnets.
    - **Linux Bastion Host:** Implemented within an Auto Scaling group, this host is pivotal for providing inbound Secure Shell (SSH) access to EC2 instances located in the private subnets.
  - **Private Subnets**
    - **Aurora DB PostgreSQL Cluster:** This cluster is the backbone of the database operations, inclusive of two DB reader nodes and a single DB writer node.
- **AWS Key Management Service (KMS)**
  - A dedicated encryption key is established using KMS.
  - This key is paramount to enable encryption at rest for the Aurora DB PostgreSQL cluster.
- **Amazon CloudWatch**
  - A vigilant monitoring system is in place to oversee the CPU utilization of the bastion host.
  - Should any anomalies be detected, an Amazon Simple Notification Service (SNS) alert is triggered.

</details>

<details>
<summary>Assignment</summary>

- **Create and submit an Azure Architecture Diagram:**
  - You are tasked with designing and submitting a `diagram` that mirrors the architecture provided - using Azure services.
- **Create and submit detailed documentation:**
  - **Service Features**
    - Examine the features and functionalities provided by the cloud service.
  - **Scalability and Performance**
    - Evaluate the service's ability to scale dynamically based on demand and handle peak workloads - think auto-scaling, load balancing, and performance metrics.
  - **Reliability and Availability**
    - Assess the uptime guarantees, service-level agreements (SLAs), and fault tolerance mechanisms.
  - **Security and Compliance**
    - Investigate encryption, access controls, authentication mechanisms, and compliance certifications.
  - **Data Storage and Management**
    - Examine the storage options provided by the service.
  - **Integration Capabilities**
    - The extent to which the service can seamlessly work with other systems and services.
  - **Cost and Pricing Model**
    - The pricing structure and associated costs for utilizing the service.
  - **Management and Monitoring**
    - Evaluate features like integration with dashboards, logging, metrics, alerts, and automation capabilities.
  - **Service-Level Agreements (SLAs)**
    - Review the SLAs provided by the cloud service for uptime, availability, performance, and support.
- **Azure Resources**
  - To facilitate a smooth transition from AWS to Azure, consider leveraging the following resources:
    - Azure for [AWS professionals](https://learn.microsoft.com/en-us/azure/architecture/aws-professional/)
    - AWS to [Azure services comparison](https://learn.microsoft.com/en-us/azure/architecture/aws-professional/services)
   
</details>

## Reference Info

<details>
<summary>Zero Trust Pillars</summary>

Microsoft Zero Trust [Whitepaper pages: 6-8](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RWJJdT)

| ZTS Pillars | Definition | Notes |
| --- | --- | --- |
| Identities | Identities—whether they represent people, workloads, endpoints, or IoT devices—define the Zero Trust control plane. When an identity attempts to access a resource, we need to verify that identity with strong authentication and ensure access is compliant and typical for that identity and follows least privilege access principles. | [Learn More](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview)
| Endpoints | Once an identity has been granted access to a resource, data can flow to a variety of different devices—from IoT devices to smartphones, BYOD to partner managed devices, and on- premises workloads to cloud hosted servers. This diversity creates a massive attack surface area, requiring we monitor and enforce device health and compliance for secure access. | [Learn More](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview)
| Networks | All data is ultimately accessed over network infrastructure. Networking controls can provide critical “in pipe” controls to enhance visibility and help prevent attackers from moving laterally across the network. Networks should be segmented (including deeper in-network micro segmentation) and real-time threat protection, end-to-end encryption, monitoring, and analytics should be employed. | [Learn More](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)
| Applications | Applications and APIs provide the interface by which data is consumed. They may be legacy on-premises, lift-and-shifted to cloud workloads, or modern SaaS applications. Controls and technologies should be applied to discover shadow IT, ensure appropriate in-app permissions, gate access based on real-time analytics, monitor for abnormal behavior, control user actions, and validate secure configuration options. | [Learn More](https://learn.microsoft.com/en-us/azure/active-directory/develop/application-model)
| Data | Ultimately, security teams are focused on protecting data. Where possible, data should remain safe even if it leaves the devices, apps, infrastructure, and networks the organization controls. Data should be classified, labeled, and encrypted, and access restricted based on those attributes. | [Learn More](https://azure.microsoft.com/en-us/products/?query=data)
| Infrastructure | Infrastructure (whether on-premises servers, cloud-based VMs, containers, or micro-services) represents a critical threat vector. Assess for version, configuration, and JIT access to harden defense, use telemetry to detect attacks and anomalies, and automatically block and flag risky behavior and take protective actions. | [Learn More](https://azure.microsoft.com/en-us/products/?query=Infrastructure)
| Policy Optimization | The organization-specific security policies applied throughout an organization's programs across the entire digital estate. The policies are optimized for business processes, governance, compliance, and the end-user experience. | [Learn More](https://azure.microsoft.com-en-us/products/azure-policy/)
| Policy Enforcement | The Zero Trust policy intercepts the request and explicitly verifies signals from all six foundational elements based on policy configuration and enforces the least privileged access. Signals include the role of the user, location, device compliance, data sensitivity, application sensitivity, and much more. In addition to telemetry and state information, the risk assessment from threat protection feeds into the policy to automatically respond to threats in real time. The policy is enforced at the time of access and continuously evaluated throughout the session. | [Learn More](https://azure.microsoft.com-en-us/products/azure-policy/)
| Threat Protection | Telemetry and analytics from all the six foundational elements feed into the threat protection system with our Zero Trust architecture. Large amounts of telemetry and analytics enriched by threat intelligence generate high-quality risk assessments that can be manually investigated or automated. The risk assessment feeds into the policy engine for real-time automated threat protection. | [Learn More](https://learn.microsoft.com-en-us/azure/security/fundamentals/threat-detection)

</details>

<details>
<summary>Possible Security Questions</summary>

This is not a complete list, and you’re not restricted to items presented here. I am providing to spark thinking.

1. What security measures are in place to protect data at rest and in transit within the cloud service?
2. Does the cloud service provider have compliance certifications relevant to my industry or regulatory requirements (e.g., GDPR, HIPAA, PCI DSS)?
3. How does the cloud service provider handle access control and authentication for user accounts and resources?
4. Are encryption mechanisms available for data stored in the cloud service? Can I bring my encryption keys?
5. What logging and auditing capabilities are provided to monitor and track activities within the cloud service?
6. Are there users for data residency and the ability to keep data within specific geographic regions or data centers?
7. How does the cloud service provider handle data backups, disaster recovery, and business continuity planning?
8. What measures are in place to protect against DDoS attacks and other security threats?
9. Can the cloud service provider provide security incident response and support in the event of a security breach?
10. Are there tools or features available for vulnerability scanning, intrusion detection, and threat intelligence within the cloud service?
11. How does the cloud service provider handle data segregation to ensure my data is isolated from other customers?
12. What are the privacy policies and data usage terms of the cloud service provider?
13. Does the provider provide security-related documentation: penetration testing reports, security white papers, or compliance attestations?
14. Are features or services available to help with identity and access management (IAM) within the cloud service?
15. How does the cloud service provider handle patch management and keep the underlying infrastructure up to date with the latest security fixes?

</details>

<details>
<summary>Additonal Links</summary>

- [Pulumi for Azure](https://www.pulumi.com/docs/clouds/azure/get-started/)
- [Infrastructure as Code with Azure and Python](https://devblogs.microsoft.com/devops/infrastructure-as-code-azure-python-wpulumi/)
- [Azure How-To Guides](https://www.pulumi.com/registry/packages/azure/how-to-guides/)
- [Pulumi GitHub Examples](https://github.com/pulumi/examples)

</details>
