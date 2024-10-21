def M_S_efectivo():
    #Proceso de venta con monto mayor
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Click(27, 7)
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Enter]")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Click(123, 16)
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Keys("agua[Tab]")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.ClickCell(4, "Descripción")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.Keys("[Enter]")
    
    #Proceso de cobro
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[F12]")
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Click(11, 14)
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Keys("1[Tab]")
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Keys("20[Tab]")
    Aliases.CCPDV.FrmCambioDinero.npnlBase.btnAceptar.ClickButton()
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Esc]")
