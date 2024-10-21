def TestLatestTicketDetails():
    # Creamos conexion a la Base de Datos
    AConnection = ADO.CreateADOConnection()
    
    AConnection.ConnectionString = "Provider=SQLOLEDB; " +\
        "Data Source=192.168.210.10; " +\
        "Initial Catalog=compucaja1801; " +\
        "User ID=consultaocs; " +\
        "Password=M1K10SK0;" +\
        "TrustServerCertificate=true;"
    
    AConnection.LoginPrompt = False
    AConnection.Open()

    # Query de consulta a Importe y Forma de pago
    query = '''SELECT TOP 1 * 
               FROM ImporteFormaPagoTicket
               WHERE FolTda_Codigo = 1801'''

    RecSet = AConnection.Execute_(query)
    
    # Asignamos los valores a una lista
    ticket_details = []
    if not RecSet.EOF:
        detail = {
            "Folio": RecSet.Fields.Item["FolConsecutivo"].Value,
            "FormaDePago": RecSet.Fields.Item["FP_Codigo"].Value,
            "Importe": RecSet.Fields.Item["IFPT_Importe"].Value,
        }
        ticket_details.append(detail)
        
    # Cerramos conexion a la DB
    AConnection.Close()  
    
    # Mostramos resultados en el log de TestComplete
    if ticket_details:
        Log.Message("Forma de Pago e Importe:")
        for detail in ticket_details:
            Log.Message(str(detail))
    
    return ticket_details if ticket_details else None
