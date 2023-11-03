## Question 1

Copy Onpremise file into a storage account name DivergenceCapstone1.Use AzCopy to copy your files from your on-premises network to the following Azure Storage services in DivergenceCapstone1 storage account:

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

| Change | Causes system downtime? |      |
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





