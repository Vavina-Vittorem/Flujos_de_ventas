def M_E_dolares():
    #Clicks the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Click(36, 16)
    #Enters '[Enter]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Enter]")
    #Enters 'agua[Tab]' in the 'txtBusqueda' object.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Keys("agua[Tab]")
    #Double-clicks the 'dgvDatos' grid cell at row 0, column 'Descripción'.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.DblClickCell(0, "Descripción")
    #Enters '[Enter]' in the 'dgvDatos' object.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.Keys("[Enter]")
    #Enters '[F12]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[F12]")
    #Enters '2[Tab]' in the 'txtFPCodigo' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Keys("2[Tab]")
    #Enters '[Tab]' in the 'txtMonto' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Keys("[Tab]")
    #Drags the 'lblCambioDesc' object.
    Aliases.CCPDV.FrmCambioDinero.npnlBase.lblCambioDesc.Drag(148, 43, 87, -1)
    #Clicks the 'lblCambioDesc' object.
    Aliases.CCPDV.FrmCambioDinero.npnlBase.lblCambioDesc.Click(235, 42)
    #Clicks the 'btnAceptar' button.
    Aliases.CCPDV.FrmCambioDinero.npnlBase.btnAceptar.ClickButton()
    #Drags the 'dgvRenglones' object.
    Aliases.CCPDV.FrmPOS.npnlBase.dgvRenglones.Drag(330, 120, 39, 0)
    #Enters '[Esc]' in the 'dgvRenglones' object.
    Aliases.CCPDV.FrmPOS.npnlBase.dgvRenglones.Keys("[Esc]")
