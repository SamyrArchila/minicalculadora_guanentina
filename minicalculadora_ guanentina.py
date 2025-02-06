import math as mt

print("---------------------------")
print("1) suma")
print("2) resta")
print("3) multiplicacion")
print("4) division")
print("5) potencia")
print("6) logaritmo")
print("--------------------------")

opc = int(input("Dijite el los numeros para realizar la operacion "))

x = int(input("Dijite el primer numero de la operacion "))
y = int(input("Dijite el segundo numero de la operacion "))

if opc == 1:
    print(f"el resultado de la suma es {(x)+(y)}")

elif opc == 2:
    print(f"el resultado de la resta es {(x)-(y)}")

elif opc == 3:
    print(f"el resultado de la multiplicacion es {(x)*(y)}")

elif opc == 4:
    if y <= 0:
        print("Error.")
    else:
        print(f"el resultado de la division es {(x)/(y)}")

elif opc == 5:
    print(f"el resultado de la potenciacion es {(x)**(y)}")

elif opc == 6:
    logaritmo = mt.log(y,x)
    print(f"el resultado del logaritmo es {logaritmo}")

else:
    print("No valido")







 