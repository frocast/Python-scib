import mi_modulo as mm
mm.colocar("Tareas/Obligatorias/test.txt", "Hola mundo\nEste es un mensaje de prueba")
mm.colocar("Tareas/Obligatorias/test2.txt", "Mas datos de prueba\n:D")
print mm.contenido("Tareas/Obligatorias/test2.txt")
print mm.contenido("Tareas/Obligatorias/test.txt")
mm.contenido_falso("Tareas/Obligatorias/numeros.txt", 10)
print mm.contenido("Tareas/Obligatorias/numeros.txt")