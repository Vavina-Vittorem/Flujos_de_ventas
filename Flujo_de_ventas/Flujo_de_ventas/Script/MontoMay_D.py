def M_S_dolares():
    #Clicks the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Click(71, 5)
    #Enters '[Enter]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Enter]")
    #Enters 'au[BS]fua[BS][BS][BS]gua[Tab][Enter]' in the 'txtBusqueda' object.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Keys("au[BS]fua[BS][BS][BS]gua[Tab][Enter]")
    #Enters '[F12]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[F12]")
    #Clicks the 'txtFPCodigo' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Click(17, 23)
    #Enters '2[Tab]' in the 'txtFPCodigo' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Keys("2[Tab]")
    #Enters '5[Tab]' in the 'txtMonto' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Keys("5[Tab]")
    #Clicks the 'lblCambioDesc' object.
    #Aliases.CCPDV.FrmCambioDinero.npnlBase.lblCambioDesc.Click(177, 39)
    #Clicks the 'btnAceptar' button.
    Aliases.CCPDV.FrmCambioDinero.npnlBase.btnAceptar.ClickButton()
    #Drags the 'dgvRenglones' object.
    Aliases.CCPDV.FrmPOS.npnlBase.dgvRenglones.Drag(302, 159, 85, -10)
    #Enters '[Esc]' in the 'dgvRenglones' object.
    Aliases.CCPDV.FrmPOS.npnlBase.dgvRenglones.Keys("[Esc]")
