def M_S_dolares():
    #Proceso de compra donde devuelve cambio
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Click(71, 5)
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Enter]")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Keys("agua[Tab][Enter]")
    
    #Proceso de pago
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[F12]")
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Click(17, 23)
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Keys("2[Tab]")
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Keys("5[Tab]")
    Aliases.CCPDV.FrmCambioDinero.npnlBase.btnAceptar.ClickButton()
    Aliases.CCPDV.FrmPOS.npnlBase.dgvRenglones.Keys("[Esc]")
