import Login
import Cancelar_compra
import Login
import Consulta_caja
import MontoEq_D
import MontoMen_D
import MontoMay_D
import Test_Tickets


def test_dolares():
    #Login.Login()
    Consulta_caja.Consulta_valores_caja()
    #Aquí va el flujo de monto menor
    MontoEq_D.M_E_dolares()
    MontoMay_D.M_S_dolares()
    Consulta_caja.Consulta_valores_caja()
    #Cancelar_compra.cancelar_compra()
    Test_Tickets.test_tickets()
    