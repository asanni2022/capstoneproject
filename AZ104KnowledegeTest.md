### Question 1

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




