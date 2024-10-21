import re

def Consulta_valores_caja():
    #Ctrl + R para hacer consulta de los valores de caja
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("^r")
    Aliases.CCPDV.FrmReportesCC.npnlBase.nvpnlReportes.ClickItem("Punto venta", "Contenido de Caja")
    
    # Extraer el texto completo del objeto 'txtReporte'
    venta_texto = Aliases.CCPDV.FrmVisorReportes.npnlBase.txtReporte.wText

    # Usar una expresión regular para buscar el valor de 'EFECTIVO'
    efectivo_match = re.search(r"_EFECTIVO\s+([\d,]+\.\d{2})", venta_texto)

    efectivo_valor = None  # Inicializar la variable para almacenar el valor de 'EFECTIVO'

    if efectivo_match:
        efectivo_valor = efectivo_match.group(1)  # Extraer el valor encontrado
        Log.Message(f"El valor de EFECTIVO es: {efectivo_valor}")
    else:
        Log.Warning("No se encontró el valor de EFECTIVO en el reporte.")
    
    # Asegurarse de cerrar la ventana antes de retornar el valor
    Aliases.CCPDV.FrmVisorReportes.npnlBase.btnCerrar.ClickButton()

    return efectivo_valor  # Retornar el valor de 'EFECTIVO' al final
