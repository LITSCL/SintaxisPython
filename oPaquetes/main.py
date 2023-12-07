#Los paquetes se deben utilizar para agrupar módulos que tengan relación entre ellos o cumplan con una finalidad similar.

from oPaquetes.paquete import calculadora, impresora

#from cl.litscl.sintaxis.oPaquetes.paquete import calculadora
#from cl.litscl.sintaxis.oPaquetes.paquete import impresora

#from paquete import calculadora
#from paquete import impresora

print(calculadora.sumar(2, 3))
print(impresora.decir_hola())