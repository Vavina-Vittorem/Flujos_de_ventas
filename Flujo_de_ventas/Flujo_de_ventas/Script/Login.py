def Login():
    #Clicks the 'lblPOS' object.
    Aliases.CCPDV.FrmPrincipal.npnlBase.lblPOS.Click(35, 7)
    #Enters the text 'CAJERO1' in the 'txtUsuario' text editor.
    Aliases.CCPDV.FrmIngreso.npnlBase.txtUsuario.SetText("CAJERO1")
    #Enters '[Tab]' in the 'txtUsuario' object.
    Aliases.CCPDV.FrmIngreso.npnlBase.txtUsuario.Keys("[Tab]")
    #Enters text in the 'txtContrasena' text editor.
    Aliases.CCPDV.FrmIngreso.npnlBase.txtContrasena.SetText(Project.Variables.Password1)
    #Enters '[Enter]' in the 'txtContrasena' object.
    Aliases.CCPDV.FrmIngreso.npnlBase.txtContrasena.Keys("[Enter]")
