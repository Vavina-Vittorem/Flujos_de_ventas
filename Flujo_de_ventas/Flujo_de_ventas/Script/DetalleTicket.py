def TestLatestTicketDetails():
    # Creamos conexion a base de datos
    AConnection = ADO.CreateADOConnection()

    AConnection.ConnectionString = "Provider=SQLOLEDB; " +\
        "Data Source=192.168.210.10; " +\
        "Initial Catalog=compucaja1801; " +\
        "User ID=consultaocs; " +\
        "Password=M1K10SK0;" +\
        "TrustServerCertificate=true;"
        
    AConnection.LoginPrompt = False
    AConnection.Open()

    #Ejecutamos Query de consulta a detalle del ticket
    query = '''SELECT TOP 1 * 
               FROM DetallesTicket
               WHERE FolTda_Codigo = 1801'''

    RecSet = AConnection.Execute_(query)
    
    #Almacenamos la info en una lista
    ticket_details = []
    if not RecSet.EOF:
        detail = {
            "Folio": RecSet.Fields.Item["FolConsecutivo"].Value,
            "Cantidad": RecSet.Fields.Item["DT_Cantidad"].Value,
            "PrecioUnitario": RecSet.Fields.Item["DT_PrecioUnitario"].Value,
            "ArtCodEscaneado": RecSet.Fields.Item["DT_ArtCodEscaneado"].Value,
            
         
        }
        ticket_details.append(detail)
    #Cerramos la conexion a la DB
    AConnection.Close() 
    
    
    #Mostramos el valor en el log de test complete
    if ticket_details:
        Log.Message("Detalles del último ticket:")
        for detail in ticket_details:
            Log.Message(str(detail))
    
    return ticket_details if ticket_details else None
