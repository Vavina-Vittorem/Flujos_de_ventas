import Login
import Cancelar_compra
import Login
import Consulta_caja_E
import MontoEq_E
import MontoMen_E
import MontoMay_E
import Test_Tickets

def test_efectivo():
    # Login.Login()

    valor_inicial = Consulta_caja_E.Consulta_valores_caja()
    Log.Message(f"Valor inicial de la caja (EFECTIVO): {valor_inicial}")
    
    # Realizar las operaciones de monto menor
    MontoEq_E.M_E_efectivo()
    MontoMay_E.M_S_efectivo()
    
    # Obtener el valor final de la caja en efectivo
    valor_final = Consulta_caja_E.Consulta_valores_caja()
    Log.Message(f"Valor final de la caja (EFECTIVO): {valor_final}")

    # Comparar el valor inicial y el valor final
    Log.Message(f"Valor inicial: {valor_inicial} y valor final de la caja:{valor_final}")

    # Cancelar_compra.cancelar_compra()
    Test_Tickets.test_tickets()
