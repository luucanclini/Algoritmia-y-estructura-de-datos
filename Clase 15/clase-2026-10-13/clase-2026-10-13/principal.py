from persona import Persona
from empleado import Empleado
from fabrica import Fabrica

p1 = Persona( "Valentino", 61.0 )
p2 = Persona( "Thiago", 92.0 )

print("p1: ", p1)
print("p2: ", p2)

print("Nombre de p1: ", p1.get_nombre())
peso = p1.get_peso()
print("Peso de p1: ", peso)

p2.set_peso(90.0)
print("Thiago luego de su cambio fisico: ", p2)

p1.engordar()
p1.engordar()
print("Valentino luego de 2 engordes: ", p1)

#p2.set_peso(-100.0)
#print("Thiago luego de la cuchara de antimateria: ", p2)

e1 = Empleado( "Maria", 56, 250000)
print("Nombre de e1: ", e1.get_nombre()) # heredado de Persona
print("Peso de e1: ", e1.get_peso()) # heredado de Persona
print("Sueldo de e1: ", e1.get_sueldo()) # programado en Empleado
print("Maria: ", e1)
print("Maria: ", str(e1))
print("Maria: ", e1.__str__())

# String multilinea
mi_mensaje = '''
Nos los representantes del pueblo de la Nación Argentina,
reunidos en Congreso General Constituyente por voluntad
y elección de las provincias que la componen,
en cumplimiento de pactos preexistentes,
con el objeto de constituir la unión nacional,
afianzar la justicia, consolidar la paz
interior, proveer a la defensa común,
promover el bienestar general, y
asegurar los beneficios de la libertad,
para nosotros, para nuestra posteridad,
y para todos los hombres del mundo que
quieran habitar en el suelo argentino:
invocando la protección de Dios,
fuente de toda razón y justicia:
ordenamos, decretamos y
establecemos esta Constitución,
para la Nación Argentina.
'''
print(mi_mensaje)

f1 = Fabrica( "DOW", "Ing White" )
e1.set_lugar_trabajo(f1)

