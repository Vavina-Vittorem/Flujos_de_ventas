def TestLatestTicket():
    # Create a Connection object
    AConnection = ADO.CreateADOConnection()
    
    # Specify the connection string
    AConnection.ConnectionString = "Provider=SQLOLEDB; " +\
        "Data Source=192.168.210.10; " +\
        "Initial Catalog=compucaja1801; " +\
        "User ID=consultaocs; " +\
        "Password=M1K10SK0;" +\
        "TrustServerCertificate=true;"
    
    # Suppress the login dialog box
    AConnection.LoginPrompt = False
    AConnection.Open()

    # Execute a simple query
    query = '''SELECT TOP 1 * FROM Tickets
               WHERE FolTda_Codigo = 1801
               ORDER BY T_Fecha DESC'''

    RecSet = AConnection.Execute_(query)
    
    # Retrieve data from RecSet before closing the connection
    latest_ticket_info = None
    if not RecSet.EOF:
        latest_ticket_info = {
            "FolConsecutivo": RecSet.Fields.Item["FolConsecutivo"].Value,
        }

        # Log the retrieved ticket information
        Log.Message("Último ticket obtenido: " + str(latest_ticket_info))
    
    AConnection.Close()  # Close the connection after processing the results
    
    return latest_ticket_info if latest_ticket_info else None


