import Login
import Cancelar_compra
import Login
import Consulta_caja_D
import MontoEq_D
import MontoMen_D
import MontoMay_D
import Test_Tickets


def test_dolares():
    #Login.Login()
    valor_inicial = Consulta_caja_D.Consulta_valores_caja()
    
    MontoEq_D.M_E_dolares()
    MontoMay_D.M_S_dolares()
    
    valor_final = Consulta_caja_D.Consulta_valores_caja()
    Log.Message(f"Valor inicial: {valor_inicial} y valor final de la caja:{valor_final}")
    
    
    #Cancelar_compra.cancelar_compra()
    Test_Tickets.test_tickets()
    