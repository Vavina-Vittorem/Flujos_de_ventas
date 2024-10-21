def TestLatestTicket():
   # Levantamos conexion a base de datos
    AConnection = ADO.CreateADOConnection()
    
    AConnection.ConnectionString = "Provider=SQLOLEDB; " +\
        "Data Source=192.168.210.10; " +\
        "Initial Catalog=compucaja1801; " +\
        "User ID=consultaocs; " +\
        "Password=M1K10SK0;" +\
        "TrustServerCertificate=true;"
        
    AConnection.LoginPrompt = False
    AConnection.Open()

    
    
    #Query de consulta de Folio
    
    query = '''SELECT TOP 1 * FROM Tickets
               WHERE FolTda_Codigo = 1801'''

    RecSet = AConnection.Execute_(query)
    
   #Asignamos el valo a una variable
    latest_ticket_info = None
    if not RecSet.EOF:
        latest_ticket_info = {
            "FolConsecutivo": RecSet.Fields.Item["FolConsecutivo"].Value,
        }

        #Mensaje en el log de test complete
        Log.Message("Último ticket obtenido: " + str(latest_ticket_info))
    #Cerramos conexion a DB
    AConnection.Close()
    return latest_ticket_info if latest_ticket_info else None


