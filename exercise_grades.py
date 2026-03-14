def grades():
    """
    Ejercicio 11 - Promedio de Calificaciones

    Dadas tres notas, calcular e imprimir:
    1. El promedio de las tres notas
    2. La nota máxima
    3. La nota mínima
    4. Cuántos puntos faltan del promedio a 10
    """
    nota1 = 8
    nota2 = 7
    nota3 = 9
    promedio = (nota1 + nota2 + nota3)/3
    notas = [8, 9, 7]
    notas_max = max(notas)
    notas_min = min(notas)
    puntos = 10 - promedio

    print(promedio)
    print(notas_max)
    print(notas_min)
    print(puntos)


grades()
   