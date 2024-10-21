import re

def Consulta_valores_caja():
    #Ctrl + R para hacer consulta de los valores de caja
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("^r")
    Aliases.CCPDV.FrmReportesCC.npnlBase.nvpnlReportes.ClickItem("Punto venta", "Contenido de Caja")
    
    # Extraer el texto completo del objeto 'txtReporte'
    venta_texto = Aliases.CCPDV.FrmVisorReportes.npnlBase.txtReporte.wText

    # Usar una expresión regular para buscar el valor de 'DOLARES'
    dolares_match = re.search(r"DOLARES\s*\n\s*\(.*\)\s+([\d,]+\.\d{2})", venta_texto)

    dolares_valor = None  # Inicializar la variable

    if dolares_match:
        dolares_valor = dolares_match.group(1)  # Extraer el valor encontrado
        Log.Message(f"El valor de DOLARES es: {dolares_valor}")
    else:
        Log.Warning("No se encontró el valor de DOLARES en el reporte.")

    # Asegurarse de que la ventana se cierra independientemente de si se encontró el valor o no
    Aliases.CCPDV.FrmVisorReportes.npnlBase.btnCerrar.ClickButton()

    return dolares_valor  # Retornar el valor después de cerrar la ventana
