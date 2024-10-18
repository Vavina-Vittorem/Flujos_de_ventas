def cancelar_compra():
    #Clicks the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Click(31, 3)
    #Enters '[Enter]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Enter]")
    #Enters 'aug[BS][BS]gua[Tab]' in the 'txtBusqueda' object.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Keys("aug[BS][BS]gua[Tab]")
    #Double-clicks the 'dgvDatos' grid cell at row 4, column 'Descripción'.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.DblClickCell(4, "Descripción")
    #Enters '[Enter]' in the 'dgvDatos' object.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.Keys("[Enter]")
    #Enters '[F2]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[F2]")
    #Clicks the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Click(22, 7)
    #Enters '[Enter]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Enter]")
    #Enters 'agua[Tab]' in the 'txtBusqueda' object.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Keys("agua[Tab]")
    #Clicks the 'dgvDatos' grid cell at row 4, column 'Descripción'.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.ClickCell(4, "Descripción")
    #Enters '![Down][Up][Enter]' in the 'dgvDatos' object.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.Keys("![Down][Up][Enter]")
    #Clicks the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Click(21, 16)
    #Enters '[Enter]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Enter]")
    #Clicks the 'txtBusqueda' object.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Click(177, 18)
    #Enters 'coca[Tab]' in the 'txtBusqueda' object.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Keys("coca[Tab]")
    #Clicks the 'dgvDatos' grid cell at row 1, column 'Descripción'.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.ClickCell(1, "Descripción")
    #Enters '[Enter]' in the 'dgvDatos' object.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.Keys("[Enter]")
    #Enters '^[F2]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("^[F2]")
    #Selects the 'PETICION DEL CLIENTE' item of the 'cmbMotivoCancelacion' combo box.
    Aliases.CCPDV.FrmMotivoCancelacion.npnlBase.cmbMotivoCancelacion.ClickItem("PETICION DEL CLIENTE")
    #Enters '[Enter]' in the 'cmbMotivoCancelacion' object.
    Aliases.CCPDV.FrmMotivoCancelacion.npnlBase.cmbMotivoCancelacion.Keys("[Enter]")
    #Clicks the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Click(24, 10)
    #Enters '[Enter]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Enter]")
    #Enters 'a[Tab]' in the 'txtBusqueda' object.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Keys("a[Tab]")
    #Clicks the 'dgvDatos' grid cell at row 3, column 'Descripción'.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.ClickCell(3, "Descripción")
    #Enters '[Enter]' in the 'dgvDatos' object.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.Keys("[Enter]")
    #Enters '[F12]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[F12]")
    #Clicks the 'btnAceptar' button.
    Aliases.CCPDV.FrmCancelados.npnlBase.btnAceptar.ClickButton()
    #Enters '1' in the 'FrmMain' object.
    Aliases.CCPDV.FrmMain.Keys("1")
    #Clicks the 'txtFPCodigo' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Click(13, 6)
    #Enters '1[Tab]' in the 'txtFPCodigo' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Keys("1[Tab]")
    #Enters '[Tab]' in the 'txtMonto' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Keys("[Tab]")
    #Clicks the 'btnAceptar' button.
    Aliases.CCPDV.FrmCambioDinero.npnlBase.btnAceptar.ClickButton()
    #Enters '[Esc]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Esc]")
