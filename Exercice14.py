age = int(input("Entrez l'âge de l'enfant : "))

if age >= 6 and age <= 7:
    print("La catégorie de l'enfant est : Poussin")
elif age >= 8 and age <= 9:
    print("La catégorie de l'enfant est : Pupile")
elif age >= 10 and age <= 11:
    print("La catégorie de l'enfant est : Minime")
elif age >= 12:
    print("La catégorie de l'enfant est : Cadet")
else:
    print("L'enfant est trop jeune.")
