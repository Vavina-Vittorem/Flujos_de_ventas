def M_S_efectivo():
    #Clicks the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Click(27, 7)
    #Enters '[Enter]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Enter]")
    #Clicks the 'txtBusqueda' object.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Click(123, 16)
    #Enters 'agua[Tab]' in the 'txtBusqueda' object.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Keys("agua[Tab]")
    #Clicks the 'dgvDatos' grid cell at row 4, column 'Descripción'.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.ClickCell(4, "Descripción")
    #Enters '[Enter]' in the 'dgvDatos' object.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.Keys("[Enter]")
    #Enters '[F12]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[F12]")
    #Enters '1' in the 'FrmMain' object.
    Aliases.CCPDV.FrmMain.Keys("1")
    #Clicks the 'txtFPCodigo' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Click(11, 14)
    #Enters '1[Tab]' in the 'txtFPCodigo' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Keys("1[Tab]")
    #Enters '20[Tab]' in the 'txtMonto' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Keys("20[Tab]")
    #Clicks the 'lblCambioDesc' object.
    #Aliases.CCPDV.FrmCambioDinero.npnlBase.lblCambioDesc.Click(202, 37)
    #Drags the 'lblCambioDesc' object.
    #Aliases.CCPDV.FrmCambioDinero.npnlBase.lblCambioDesc.Drag(149, 35, 61, 1)
    #Clicks the 'btnAceptar' button.
    Aliases.CCPDV.FrmCambioDinero.npnlBase.btnAceptar.ClickButton()
    #Enters '[Esc]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Esc]")
