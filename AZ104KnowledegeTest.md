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




