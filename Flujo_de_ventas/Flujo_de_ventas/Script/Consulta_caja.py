def Consulta_valores_caja():
    #Enters '^r' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("^r")
    #Clicks the 'Contenido de Caja' item of 'Punto venta' group of the 'nvpnlReportes' bar.
    Aliases.CCPDV.FrmReportesCC.npnlBase.nvpnlReportes.ClickItem("Punto venta", "Contenido de Caja")
    #Drags the 'txtReporte' object.
    Aliases.CCPDV.FrmVisorReportes.npnlBase.txtReporte.Drag(142, 162, 55, -3)
    #Clicks the 'btnCerrar' button.
    Aliases.CCPDV.FrmVisorReportes.npnlBase.btnCerrar.ClickButton()
