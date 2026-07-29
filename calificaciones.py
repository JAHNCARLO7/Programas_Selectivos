pa = float(input("Ingresa tu calificación del parcial de 0 a 100: "))
pro = float(input("Ingresa tu calificación del proyecto de 0 a 100): "))
exa = float(input("Ingresa tu calificación del examen final de 0 a 100: "))

if (pa < 0 or pa> 100) or (pro < 0 or pro> 100) or (exa< 0 or exa > 100):
    print("Error: las notas deben estar entre 0 y 100")
else:
    cal_final = (pa * 0.4) + (pro * 0.3) + (exa* 0.3)
    print("Nota final:", cal_final)
     