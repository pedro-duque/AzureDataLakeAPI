import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="AzureDataLakeAPI", auth_level=func.AuthLevel.ANONYMOUS)
def AzureDataLakeAPI(req: func.HttpRequest) -> func.HttpResponse:
    from Modules.DataLakeConnect.AzureDataLake import DuckDBToAzureDL
    logging.info('Python HTTP trigger function processed a request.')

    path = req.params.get('path')
    if not path:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            path = req_body.get('path')

    if path:
        import os
        
        connection_azure_dl = DuckDBToAzureDL(os.environ["CUSTOMCONNSTR_AzureDataLake"])
        query = connection_azure_dl.ReadDLTable(path, req.params.get('format'))
        
        if query["Status"] == True:
            
            return func.HttpResponse(
                body= str(query["Dataframe"]),
                mimetype="application/json",
                status_code=200
            )
        else:
            return func.HttpResponse(
                body= str(query["Error"]),
                mimetype="application/json",
                status_code=404
            )
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a path and a format in the query string or in the request body for a personalized response.",
             status_code=200
        )