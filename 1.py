answer=("1")
while answer==("1"):
    answer= input ("te gustaria saber cuanto gastas de combustible por kilometro preciona 1")
    print (" ingresa lo siguiente")
    
    c = int(answer)
    if  (c == 1):
        kilometros=float(input("Kilómetros recorridos:"))
        litros=float(input("Litros de combustible gastados:"))
        total= kilometros/litros
        print("El consumo por kilómetro es de")
        print(total)
    else:
        print ("Hasta Luego")
