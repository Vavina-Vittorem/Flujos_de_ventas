def Mixto_2_elementos_OK():
    #Clicks the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Click(19, 3)
    #Enters '[Enter]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Enter]")
    #Enters 'cococ[BS][Tab][Enter]' in the 'txtBusqueda' object.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Keys("cococ[BS][Tab][Enter]")
    #Enters '[F12]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[F12]")
    #Enters '2[Tab]' in the 'txtFPCodigo' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Keys("2[Tab]")
    #Enters '3[Tab]' in the 'txtMonto' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Keys("3[Tab]")
    #Enters '1[Tab]' in the 'txtFPCodigo' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Keys("1[Tab]")
    #Enters '[Tab]' in the 'txtMonto' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Keys("[Tab]")
    #Clicks the 'btnAceptar' button.
    Aliases.CCPDV.FrmCambioDinero.npnlBase.btnAceptar.ClickButton()
    #Enters '[Esc]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Esc]")
