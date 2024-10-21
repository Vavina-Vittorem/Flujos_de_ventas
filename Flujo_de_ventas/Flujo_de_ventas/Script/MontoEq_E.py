def M_E_efectivo():
    #Flujo de venta con monto equivalente
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Click(42, 18)
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Enter]")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Click(99, 6)
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Keys("agua[Tab]")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.ClickCell(4, "Descripción")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.dgvDatos.Keys("[Enter]")
    
    #Proceso de cobro
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[F12]")
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Click(15, 11)
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Keys("1[Tab]")
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Keys("[Tab]")
    Aliases.CCPDV.FrmCambioDinero.npnlBase.btnAceptar.ClickButton()
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Esc]")
