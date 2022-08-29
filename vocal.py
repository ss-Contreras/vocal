letra = input("Digite una letra: ")

def esVocal(letra):
    letra.lower() in ['a', 'e', 'i', 'o', 'u']

    if esVocal(letra):
        print("es vocal")
    else:
        print("No es vocal")

esVocal()