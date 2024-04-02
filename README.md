# Azure Data Lake API

This Python package provides an Azure Function named `AzureDataLakeAPI` that serves as an HTTP API endpoint for retrieving data from Azure Data Lake Storage (ADLS). It enables users to query data stored in ADLS and retrieve it in JSON format through HTTP requests.

## Installation

This project is designed to be deployed as an Azure Function, and it's not intended for direct installation or usage as a standalone package.

## Usage

### HTTP API Endpoint

The `AzureDataLakeAPI` endpoint exposes the functionality to retrieve data from ADLS via HTTP requests. It expects the following parameters:

- **path**: The path to the data in ADLS.
- **format**: The format of the data (currently supports "parquet").

#### Example Request:

```http
GET /api/AzureDataLakeAPI?path=<Path_to_data>&format=<Data_format>
```

#### Example Response:

```json
{
  "Status": true,
  "Dataframe": "[{\"column1\": value1, \"column2\": value2, ...}]"
}
```

### DuckDBToAzureDL Class

The `DuckDBToAzureDL` class provides the underlying functionality for connecting to DuckDB and querying data from ADLS. It has the following methods:

- **\_\_init\_\_**: Initializes the connection with the provided connection string.
- **Connect**: Connects to DuckDB.
- **ReadDLTable**: Reads a table from ADLS based on the specified path and format.

## Note

Ensure that you have the necessary permissions and configurations set up in your Azure environment to access Azure Data Lake Storage.

## Dependencies

- `azure.functions`: Azure Functions SDK for Python
- `duckdb`: DuckDB for querying data
- `adlfs`: Azure Blob File System for accessing data in ADLS

## Deployment

To deploy this Azure Function, you can package the project and deploy it to Azure Functions using tools such as Azure CLI, Visual Studio Code, or Azure DevOps.

## Disclaimer

This project is provided as-is, without any warranties or guarantees. Use it at your own risk.
