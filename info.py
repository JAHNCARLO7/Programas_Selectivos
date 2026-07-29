
consulta = input("Ingrese nombre de artista, película o serie: ").lower()

match consulta:
    case "flash":
        info = "Serie/película del velocista escarlata de DC Comics."
    case "spiderman":
        info = "Película del superhéroe arácnido de Marvel."
    case "friends":
        info = "Famosa comedia de situación sobre un grupo de amigos en Nueva York."
    case "the walking dead":
        info = "Serie dramática de supervivencia sobre un apocalipsis zombi."
    case "titanes":
        info = "Serie basada en los Jóvenes Titanes de DC Comics."
    case _:
        info = "No se encontró información."

print("Información:", info)