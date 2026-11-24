from persona import Persona

personas = {
    47117363: Persona('lucia',50),
    18398937: Persona('esteban',80),
    22507352: Persona('marisa',70),
    47480155: Persona('leonel',70),
    44453822: Persona('camilo',90)
}

#listado
def listarPersonas(d):
    for k in d.values():
        print(k,'-',end='')
    print()

listarPersonas(personas)

def encontrarPersona(d,dni):
    print(d[dni])
    return(d[dni])

def cambiarPeso(peso,persona):
    persona.set_peso(peso)
    print (persona)

dni = int(input('ingrese un dni para q la persona lo salude: '))
persona1 = encontrarPersona(personas,dni)
peso = int(input('ingrese el nuevo peso de la persona:'))
cambiarPeso(peso,persona1)
