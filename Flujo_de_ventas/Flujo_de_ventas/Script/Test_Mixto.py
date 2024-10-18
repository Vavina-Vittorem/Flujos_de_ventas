import Login
import Cancelar_compra
import Login
import Consulta_caja
import Mix_2_Elem
import Mix_3_Elem

def test_mixto():
    #Login.Login()
    Consulta_caja.Consulta_valores_caja()
    #ambos fallan en la parte automatizada, de forma manual no
    #sobre todo el mix_3_elem fallara porque mezcla el uso de tarjeta test no soporta el pinpad
    Mix_2_Elem.Mixto_2_elementos_OK()
    Mix_3_Elem.Mixto_3_elementos_NOT()
    #Cancelar_compra.cancelar_compra()