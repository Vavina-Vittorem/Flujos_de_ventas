def Flujo_Tarjeta():
    #Proceso de venta con tarjeta
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Click(49, 10)
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Enter]")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Keys("sabriton[Tab][Enter]")
    
    #Proceso de cobro
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("^[ReleaseLast][F12]")
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Click(19, 13)
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Keys("3[Tab]")
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Keys("[Tab]")
    Aliases.CCPDV.FrmMensaje.pictureBox1.Click(217, 51)
    Aliases.CCPDV.dlgCOMPUCAJAnet.DblClick(185, 68)
    Aliases.CCPDV.dlgCOMPUCAJAnet.btnAceptar.ClickButton()
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Click(71, 19)
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Keys("[Esc]")
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Keys("[BS]1|[Tab]")
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Keys("[Tab]")
    Aliases.CCPDV.FrmCambioDinero.npnlBase.btnAceptar.ClickButton()
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Esc]")
