def TestLatestTicketDetails():
    #Creamos conexion a Base de Datos
    AConnection = ADO.CreateADOConnection()

    AConnection.ConnectionString = "Provider=SQLOLEDB; " +\
        "Data Source=192.168.210.10; " +\
        "Initial Catalog=compucaja1801; " +\
        "User ID=consultaocs; " +\
        "Password=M1K10SK0;" +\
        "TrustServerCertificate=true;"
    
    AConnection.LoginPrompt = False
    AConnection.Open()

    #Ejecutamos Query de consulta a Impuestos Aplicables al ticket
    query = '''SELECT TOP 1 * 
               FROM ImpuestosT
               WHERE FolTda_Codigo = 1801'''
               
    RecSet = AConnection.Execute_(query)
    
    ticket_details = []
    if not RecSet.EOF:
        detail = {
            "Folio": RecSet.Fields.Item["FolConsecutivo"].Value,
            "CodigoDeImpuesto": RecSet.Fields.Item["Imp_Codigo"].Value,
            "Descripcion": RecSet.Fields.Item["Imp_Descripcion"].Value,
        }
        ticket_details.append(detail)
        
    #Cerramos conexion a DB
    AConnection.Close()  
    
    # Mostramos resultados en el log de test complete
    if ticket_details:
        Log.Message("Impuesto Aplicable:")
        for detail in ticket_details:
            Log.Message(str(detail))
    
    return ticket_details if ticket_details else None