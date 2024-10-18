def M_E_efectivo():
    #Clicks the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Click(42, 18)
    #Enters '[Enter]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Enter]")
    #Clicks the 'txtBusqueda' object.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Click(99, 6)
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
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Click(15, 11)
    #Enters '1[Tab]' in the 'txtFPCodigo' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Keys("1[Tab]")
    #Enters '[Tab]' in the 'txtMonto' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Keys("[Tab]")
    #Clicks the 'lblCambioDesc' object.
    #Aliases.CCPDV.FrmCambioDinero.npnlBase.lblCambioDesc.Click(213, 10)
    #Clicks the 'btnAceptar' button.
    Aliases.CCPDV.FrmCambioDinero.npnlBase.btnAceptar.ClickButton()
    #Enters '[Esc]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Esc]")
