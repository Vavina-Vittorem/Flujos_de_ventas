def Login():
    #Login con credenciales validas.
    Aliases.CCPDV.FrmPrincipal.npnlBase.lblPOS.Click(35, 7)
    Aliases.CCPDV.FrmIngreso.npnlBase.txtUsuario.SetText("CAJERO1")
    Aliases.CCPDV.FrmIngreso.npnlBase.txtUsuario.Keys("[Tab]")
    Aliases.CCPDV.FrmIngreso.npnlBase.txtContrasena.SetText(Project.Variables.Password1)
    Aliases.CCPDV.FrmIngreso.npnlBase.txtContrasena.Keys("[Enter]")
