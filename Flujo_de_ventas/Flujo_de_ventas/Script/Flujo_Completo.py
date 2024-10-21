import Login
import Cancelar_compra
import Consulta_caja_E
import Test_Dolares
import Test_Efectivo
import Test_Tarjeta
import Test_Mixto


def flujo_completo():
    Login.Login()
    Test_Efectivo.test_efectivo()
    Test_Dolares.test_dolares()
    Test_Tarjeta.test_tarjeta()
    #Test_Mixto.test_mixto()
    Cancelar_compra.cancelar_compra()
    
    