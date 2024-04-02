class DuckDBToAzureDL:
    def __init__(self, ConnectionString: str) -> property: 
        self.ConnectionString = ConnectionString

        import duckdb
        from adlfs.spec import AzureBlobFileSystem

        connection = duckdb.connect()
        connection.register_filesystem(AzureBlobFileSystem(connection_string=self.ConnectionString))

        self.Connection = connection

    def Connect(self) -> classmethod:
    
        return self.Connection
    
    def ReadDLTable(self, path: str, format: str) -> classmethod:

        if format == "parquet":

            try:
                duck_df = self.Connection.sql(f'''
                SELECT * FROM read_parquet('abfs://{path}*.parquet')
                ''').df()
                return {"Status": True, "Dataframe": duck_df.to_json(orient="records")}
            
            except Exception as e:
                return {"Status": False, "Error": str(e)}
        
        else:
            return {"Status": False, "Error": "Data format not yet supported"}