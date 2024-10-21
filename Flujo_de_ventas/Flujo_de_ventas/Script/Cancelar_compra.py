def cancelar_compra():
    #Ingresamos en el buscador el artículo a cancelar.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Click(31, 3)
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Enter]")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Keys("agua[Tab]")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.DblClickCell(4, "Descripción")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.Keys("[Enter]")
    
    
    #Probamos cancelar 1 elemento con F2
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[F2]")
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Click(22, 7)
    
    #Buscamos y añadimos 2 articulos
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Enter]")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Keys("agua[Tab]")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.ClickCell(4, "Descripción")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.Keys("![Down][Up][Enter]")
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Click(21, 16)
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Enter]")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Click(177, 18)
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Keys("coca[Tab]")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.ClickCell(1, "Descripción")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.Keys("[Enter]")
    
    # Probamos cancelar todos los articulos con Ctrl + F12
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("^[F2]")
    Aliases.CCPDV.FrmMotivoCancelacion.npnlBase.cmbMotivoCancelacion.ClickItem("PETICION DEL CLIENTE")
    Aliases.CCPDV.FrmMotivoCancelacion.npnlBase.cmbMotivoCancelacion.Keys("[Enter]")
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Click(24, 10)
    
    
    #Hacemos un proceso de compra normal para que no obstruya pruebas futuras, porque al procesar compra salta la ventana de articulos cancelados.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Enter]")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Keys("a[Tab]")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.ClickCell(3, "Descripción")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.Keys("[Enter]")
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[F12]")
    Aliases.CCPDV.FrmCancelados.npnlBase.btnAceptar.ClickButton()
    Aliases.CCPDV.FrmMain.Keys("1")
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Click(13, 6)
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Keys("1[Tab]")
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Keys("[Tab]")
    Aliases.CCPDV.FrmCambioDinero.npnlBase.btnAceptar.ClickButton()
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Esc]")
