def TestLatestTicketDetails():
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

    # Execute a query to get the details of the latest ticket
    query = '''SELECT TOP 1 * 
               FROM DetallesTicket
               WHERE FolTda_Codigo = 1801 
               ORDER BY FolConsecutivo DESC'''

    RecSet = AConnection.Execute_(query)
    
    # Retrieve data from RecSet before closing the connection
    ticket_details = []
    if not RecSet.EOF:
        detail = {
            "Folio": RecSet.Fields.Item["FolConsecutivo"].Value,
            "Cantidad": RecSet.Fields.Item["DT_Cantidad"].Value,
            "PrecioUnitario": RecSet.Fields.Item["DT_PrecioUnitario"].Value,
            "ArtCodEscaneado": RecSet.Fields.Item["DT_ArtCodEscaneado"].Value,
            
         
        }
        ticket_details.append(detail)
    
    AConnection.Close()  # Close the connection after processing the results
    
    # Log the ticket details to TestComplete
    if ticket_details:
        Log.Message("Detalles del último ticket:")
        for detail in ticket_details:
            Log.Message(str(detail))
    
    return ticket_details if ticket_details else None
