# Flujo de Testeo Automatizado para Ventas PDV

Este proyecto contiene un flujo de pruebas automatizadas para el sistema de ventas PDV. El flujo está diseñado para probar diferentes métodos de pago y escenarios de cancelación utilizando TestComplete y Python.

## Requisitos Previos

- **TestComplete** instalado en tu máquina.
- Python configurado con las rutas necesarias para ejecutar los scripts.
- Conexión al entorno de pruebas del sistema PDV.
- VPN activada, conectada y con los permisos necesarios
- Permisos para la Base de Datos 1801

## Estructura del Proyecto

El flujo de pruebas se compone de varios módulos, cada uno encargado de una funcionalidad específica del sistema de ventas. A continuación se listan los módulos:

- `Login.py` - Maneja el inicio de sesión en el sistema.
- `Cancelar_compra.py` - Realiza la cancelación de una compra.
- `Consulta_caja.py` - Realiza consultas sobre el estado de caja.
- `Test_Dolares.py` - Pruebas de pagos realizados en dólares.
- `Test_Efectivo.py` - Pruebas de pagos realizados en efectivo.
- `Test_Tarjeta.py` - Pruebas de pagos realizados con tarjeta.
- `Test_Mixto.py` - Pruebas de pagos mixtos.

## Flujo de Pruebas

El flujo principal de pruebas está definido en el archivo `flujo_completo.py` y sigue los siguientes pasos:

1. **Login** - Se inicia sesión en el sistema.
2. **Test_Efectivo** - Se ejecutan las pruebas de pago en efectivo.
3. **Test_Dolares** - Se ejecutan las pruebas de pago en dólares.
4. **Test_Tarjeta** - Se ejecutan las pruebas de pago con tarjeta.
5. **Cancelar_compra** - Se realiza la cancelación de la compra.
   
**Nota:** El test de pagos mixtos (`Test_Mixto`) está comentado debido a errores conocidos que deben resolverse.

## Cómo Ejecutar el Flujo de Pruebas

Para ejecutar el flujo de pruebas, asegúrate de que todos los módulos estén correctamente importados y luego ejecuta el archivo principal:

```bash
python flujo_completo.py o directamente en la aplicación testComplete dando click en "run" el logo de la flecha verde en la parte superior.


## Errores Conocidos y Soluciones

Test Mixto: Actualmente, las pruebas de pago mixto están fallando debido a problemas con flujos interrumpidos de pago con menor cantidad.
Tickets: Falta una revisión exhaustiva de los tickets generados y de su registro en la base de datos.

## Referencias
Basado en el documento PDV_Ventas_PR_Casos de pruebas.xlsx, el cual detalla los escenarios de prueba y los resultados esperados para cada caso.
Para más detalles, consulta el documento mencionado anteriormente.