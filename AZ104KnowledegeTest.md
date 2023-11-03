## Question 1
Your company has an Azure Storage account named DivergenceCapstone1. You have to copy your files hosted on your on-premises network to DivergenceCapstone1 using AzCopy. What Azure Storage services will you be able to copy your data into?


### Answer

Copy Onpremise file into a storage account name DivergenceCapstone1. Use AzCopy to copy your files from your on-premises network to the following Azure Storage services in DivergenceCapstone1 storage account:

  - * Blob Storage
  - * File Storage
  - * Data Lake Storage Gen2

** To copy your files to Azure Blob Storage using AzCopy:**

1. Open a command prompt or PowerShell window.
2. Navigate to the directory where you installed AzCopy.
3. Run the following command:

```
azcopy copy <source path> <destination path>
```

For example, to copy all of the files in the `C:\MyFiles` directory to your Blob Storage account, you would run the following command:

```
azcopy copy C:\MyFiles https://divergencecapstone1.blob.core.windows.net/mycontainer/
```

**To copy your files to Azure File Storage using AzCopy:**

1. Open a command prompt or PowerShell window.
2. Navigate to the directory where you installed AzCopy.
3. Run the following command:

```
azcopy copy <source path> <destination path>
```

For example, to copy all of the files in the `C:\MyFiles` directory to your File Storage account, you would run the following command:

```
azcopy copy C:\MyFiles https://divergencecapstone1.file.core.windows.net/myshare/
```

**To copy your files to Azure Data Lake Storage Gen2 using AzCopy:**

1. Open a command prompt or PowerShell window.
2. Navigate to the directory where you installed AzCopy.
3. Run the following command:

```
azcopy copy <source path> <destination path>
```

For example, to copy all of the files in the `C:\MyFiles` directory to your Data Lake Storage Gen2 account, you would run the following command:

```
azcopy copy C:\MyFiles https://divergencecapstone1.dfs.core.windows.net/myfilesystem/
```

## Question 2

Your company has 12 peered virtual networks in your Azure subscription. You plan to deploy a network security group for each virtual network. There is a compliance requirement that port 80 should be automatically blocked between virtual networks whenever a new network security group is created. The solution must minimize administrative effort. Solution: You configure the network security group (NSG) flow log to automatically block port 80. Does the solution meet the goal?

### Answer
The provided solution does not meet the stated goal. Configuring the Network Security Group (NSG) flow log to automatically block port 80 does not ensure that port 80 is automatically blocked between virtual networks whenever a new NSG is created.
Here's why:

1. NSG Flow Logs: NSG flow logs are used for monitoring and analyzing network traffic through NSGs. They capture information about allowed and denied traffic but do not automatically enforce network security rules.
2. Creation of New NSGs: When you create a new NSG, it doesn't inherently affect the existing NSGs or their rules. NSG rules are specific to the NSG they are associated with, and creating a new NSG does not automatically block port 80 traffic between virtual networks.

To meet the compliance requirement and minimize administrative effort:
   - **Azure Policy or a custom automation script

Steps:

   - Create an Azure Policy definition that denies inbound traffic on port 80.
   - Assign the Azure Policy definition to the Azure Management Group that contains all of your peered virtual networks.
   - Whenever a new network security group is created within the Azure Management Group, the Azure Policy definition will be applied, and inbound traffic on port 80 will be automatically blocked.

Azure Policy:  define a policy that ensures that port 80 traffic between virtual networks is denied in NSG rules, and this policy would apply to all NSGs when created or modified. This way, it ensures automatic compliance with the required network security rules whenever new NSGs are created.

Create the Azure Policy definition and assigned it to the Azure Management Group, all new network security groups within the Azure Management Group will automatically block port 80.


## Question 3
Business-critical application hosted in a virtual machine that is associated with Azure subscription. The virtual machine has a managed disk and a network interface. You are planning to make the following changes: create and attach a new disk, change the VM size, detach a network interface, move the VM to a new resource group, add a Desired State Configuration (DSC) extension. Which of the following changes would cause system downtime?

### Answer
1. **Change the VM size:** Resizing a virtual machine involves stopping the VM, changing its size, and then starting it again. During this process, the VM is unavailable, causing system downtime.Changing the VM size. All other changes can be made without causing system downtime.

| Change | Causes system downtime |      |
| ----- | ----- | ----- |
| Create and attach a new disk | No |
| Change the VM size | Yes |
| Detach a network interface | No |
| Move the VM to a new resource group | No |
| Add a DSC extension | No |

Changing the VM size causes system downtime because Azure needs to stop the VM to resize the underlying hardware. All other changes can be made without stopping the VM.

Here are some tips for minimizing system downtime when changing the VM size:
  - * Use a live migration to resize the VM. Live migration allows Azure to move the VM to a new host without stopping it.
  - * Use an autoscaling group to resize the VM. An autoscaling group can automatically resize VMs based on predefined rules.
  - * Use a load balancer to distribute traffic across multiple VMs. This will allow you to resize one VM at a time without impacting your users.

The other changes you mentioned can generally be performed without causing system downtime:

- **Create and attach a new disk:** You can add a new data disk to a running VM without causing downtime. However, you might need to perform configuration changes inside the VM to use the new disk effectively.

- **Detach a network interface:** Detaching a network interface can be done without causing system downtime. However, it may affect the network connectivity of the VM if it relies on the detached interface.

- **Move the VM to a new resource group:** Moving a VM to a new resource group can be done without causing system downtime.

- **Add a Desired State Configuration (DSC) extension:** Adding or updating a DSC extension should not cause system downtime by itself. However, the specific configurations applied by DSC extensions can have varying impacts on system availability, depending on the changes they make.



## Question 4
You plan to migrate your business-critical application to Azure virtual machines. You need to make sure that at least two VMs are available during planned Azure maintenance. What should you do?

### Answer
To make sure that at least two VMs are available during planned Azure maintenance, you can use the following methods:

* **Availability zones:** Deploy your VMs in two different availability zones. Availability zones are physically isolated locations within an Azure region. If there is planned maintenance in one availability zone, your VMs in the other availability zone will still be available.
* **Availability sets:** Deploy your VMs in an availability set. An availability set is a logical grouping of VMs that are spread across multiple availability zones. Availability sets help to ensure that your VMs are not all affected by the same planned maintenance event.
* **Managed availability sets:** Use managed availability sets. Managed availability sets are a premium feature that provides even more protection against planned maintenance. Managed availability sets will automatically restart your VMs in another availability zone if there is planned maintenance in the availability zone where they are currently running.
* **Use a load balancer to distribute traffic across your VMs.** This will help to ensure that your application is still available even if one or more of your VMs are unavailable.
* **Use a health probe to monitor your VMs.** A health probe is a test that Azure performs to check the health of your VMs. If a VM fails the health probe, Azure will automatically restart it.
* **Use Azure Monitor to receive alerts about planned maintenance events.** Azure Monitor can send you alerts via email, SMS, or webhook. This will give you time to take corrective action before planned maintenance begins.

Here are the steps to deploy your application to two different availability zones:

1. Create a virtual network with at least two subnets in different availability zones.
2. Deploy two VMs in the different subnets.
3. Deploy your application to both VMs.



## Question 5
You are managing 50 virtual machines. You need to identify idle and underutilized resources to reduce the overall costs of your account. The service tier of your development virtual machines must also be changed to a less expensive offering. What Azure service should you use?

### Answer
To identify idle and underutilized resources and get recommendations for optimizing your Azure resources, you should use "Azure Advisor." Azure Advisor is a service that provides personalized recommendations based on your Azure usage and configurations. It analyzes your resource utilization, configurations, and other factors to help you optimize your Azure environment, reduce costs, and improve overall efficiency.

Azure Advisor provides recommendations in various categories, including:

1. **Cost:** It helps you identify idle or underutilized resources and provides recommendations for cost savings, such as resizing or deallocating VMs, and rightsizing services.

2. **Security:** It offers security-related recommendations to help you enhance your security posture.

3. **Performance:** It provides guidance on improving the performance of your resources.

4. **High Availability:** It offers suggestions to enhance the reliability and availability of your services.

5. **Operational Excellence:** Recommendations for operational efficiency and best practices.

Azure Advisor will automatically change the service tier of your development virtual machines to a less expensive offering. It will also start or stop your virtual machines based on your usage patterns.

Advisor looks at the following factors:
  **CPU utilization: Advisor looks at the CPU utilization of your VMs to identify VMs that are underutilized.

  **Disk utilization: Advisor looks at the disk utilization of your VMs to identify VMs that are underutilized.

  **Network traffic: Advisor looks at the network traffic of your VMs to identify VMs that are underutilized.











