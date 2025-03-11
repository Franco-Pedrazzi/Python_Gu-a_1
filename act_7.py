nombre=input("Inserte su nombre ")
edad=int(input("Inserte su edad "))
ciudad=input("Inserte su ciudad de residencia ")

print("Hola",nombre,"edad:",edad,"ciudad:",ciudad)
if edad>18:
    print("Felicidades tienes mas de 18")

if edad%5==0:
    print("Felicidades tu edad es multiplo de 5")