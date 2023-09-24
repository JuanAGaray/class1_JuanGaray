meme_dict = {
            "Try": "Anotación",
            "Tackle": "Acto de derribar al oponente que tiene el balón",
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")


if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Palabra no encontrada, preguntale a un programador joven")
