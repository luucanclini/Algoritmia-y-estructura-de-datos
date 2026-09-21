examen = {'Andrew', 'Kirsty', 'Beth', 'Emily', 'Sue'}
proyecto = {'Kirsty', 'Emily', 'Ian', 'Stuart'}

a = examen & proyecto
b = examen - proyecto
c = proyecto - examen
d = examen|proyecto
e = examen^proyecto

print(' estudiantes tomaron el examen y presentaron un proyecto: ', a, 'cantidad: ',len(a))
print(' estudiantes s ́olo tomaron el examen: ',b, 'cantidad: ',len(b))
print(' estudiantes s ́olo presentaron el proyecto: ',c, 'cantidad: ',len(c))
print('estudiantes que tomaron uno (o ambos) del examen y el proyecto: ',d, 'cantidad: ',len(d))
print('estudiantes que tomaron cualquiera de los dos (pero no ambos) el examen y el proyecto: ',e, 'cantidad: ',len(e))
