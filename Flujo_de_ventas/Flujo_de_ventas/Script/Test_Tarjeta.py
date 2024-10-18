import Login
import Cancelar_compra
import Consulta_caja
import Tarjeta
import Test_Tickets

def test_tarjeta():
    #Login.Login()
    Consulta_caja.Consulta_valores_caja()
    Tarjeta.Flujo_Tarjeta()
    #se supone se revisa el contenido en caja
    #no cambia porque no se efectua la venta
    Consulta_caja.Consulta_valores_caja()
    #Cancelar_compra.cancelar_compra()
    #pendiente de añadir los tickets pues no completa la compra como tal
    
    