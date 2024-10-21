def TestLatestTicketDetails():
    #Creamos conexion a DB
    AConnection = ADO.CreateADOConnection()
    
    AConnection.ConnectionString = "Provider=SQLOLEDB; " +\
        "Data Source=192.168.210.10; " +\
        "Initial Catalog=compucaja1801; " +\
        "User ID=consultaocs; " +\
        "Password=M1K10SK0;" +\
        "TrustServerCertificate=true;"
    
    AConnection.LoginPrompt = False
    AConnection.Open()

    #Corremos Query de busqueda para Tasa y total de impuestos aplicables
    query = '''SELECT TOP 1 * 
               FROM TasasImpuestosT
               WHERE FolTda_Codigo = 1801'''

    RecSet = AConnection.Execute_(query)
    
    ticket_details = []
    if not RecSet.EOF:
        detail = {
            "Folio": RecSet.Fields.Item["FolConsecutivo"].Value,
            "DescripcionDelImpuesto": RecSet.Fields.Item["TI_Descripcion"].Value,
            "ImporteDelImpuesto": RecSet.Fields.Item["TI_ImporteTotal"].Value,
            
         
        }
        ticket_details.append(detail)
    
    #Cerramos DB
    AConnection.Close()
    
    #Mostramos en log de test compelete el resultado
    if ticket_details:
        Log.Message("Tasa de impuesto e Importe del Impuesto:")
        for detail in ticket_details:
            Log.Message(str(detail))
    
    return ticket_details if ticket_details else None