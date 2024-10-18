import Login
import Cancelar_compra
import Login
import Consulta_caja
import MontoEq_E
import MontoMen_E
import MontoMay_E
import Test_Tickets

def test_efectivo():
    #Login.Login()
    Consulta_caja.Consulta_valores_caja()
    #Aquí va el flujo de monto menor
    MontoEq_E.M_E_efectivo()
    MontoMay_E.M_S_efectivo()
    Consulta_caja.Consulta_valores_caja()
    #Cancelar_compra.cancelar_compra()
    Test_Tickets.test_tickets()