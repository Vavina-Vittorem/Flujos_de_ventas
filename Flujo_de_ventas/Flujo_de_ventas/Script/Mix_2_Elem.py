def Mixto_2_elementos_OK():
    #Proceso mixto 2 elemetos fallido por impedimento de cobro mixto
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Click(19, 3)
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Enter]")
    Aliases.CCPDV.FrmBuscadorArticulosReducido.npnlBase.txtBusqueda.Keys("coco[Tab][Enter]")
    
    #Proceso de cobro
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[F12]")
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Keys("2[Tab]")
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Keys("3[Tab]")
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtFPCodigo.Keys("1[Tab]")
    Aliases.CCPDV.FrmSubTotal.npnlBase.pnlRenglones.RenglonSubtotal.txtMonto.Keys("[Tab]")
    Aliases.CCPDV.FrmCambioDinero.npnlBase.btnAceptar.ClickButton()
    Aliases.CCPDV.FrmPOS.npnlBase.txtIngreso.Keys("[Esc]")
