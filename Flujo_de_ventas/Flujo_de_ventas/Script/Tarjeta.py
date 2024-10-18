def Flujo_Tarjeta():
    #Clicks the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Click(49, 10)
    #Enters '[Enter]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Enter]")
    #Enters 'sabriton[Tab][Enter]' in the 'txtBusqueda' object.
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Keys("sabriton[Tab][Enter]")
    #Enters '^[ReleaseLast][F12]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("^[ReleaseLast][F12]")
    #Clicks the 'txtFPCodigo' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Click(19, 13)
    #Enters '3[Tab]' in the 'txtFPCodigo' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Keys("3[Tab]")
    #Enters '[Tab]' in the 'txtMonto' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Keys("[Tab]")
    #Clicks the 'pictureBox1' object.
    Aliases.CCPDV.FrmMensaje.pictureBox1.Click(217, 51)
    #Double-clicks the 'dlgCOMPUCAJAnet' object.
    Aliases.CCPDV.dlgCOMPUCAJAnet.DblClick(185, 68)
    #Clicks the 'btnAceptar' button.
    Aliases.CCPDV.dlgCOMPUCAJAnet.btnAceptar.ClickButton()
    #Clicks the 'txtMonto' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Click(71, 19)
    #Enters '[Esc]' in the 'txtMonto' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Keys("[Esc]")
    #Enters '[BS]1|[Tab]' in the 'txtFPCodigo' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Keys("[BS]1|[Tab]")
    #Enters '[Tab]' in the 'txtMonto' object.
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Keys("[Tab]")
    #Clicks the 'btnAceptar' button.
    Aliases.CCPDV.FrmCambioDinero.npnlBase.btnAceptar.ClickButton()
    #Enters '[Esc]' in the 'txtIngreso' object.
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Esc]")
