#La compañía Telefónica le pide desarrollar un programa que permita calcular el monto a 
# pagar por los minutos hablados de cada cliente. El programa debe preguntar por el total de 
# los minutos hablados en horario DIA y en horario NOCHE. Luego, se debe mostrar en cuanto excede en horario
# DIA, NOCHE y el valor final a pagar (ver ejemplos de ejecución). 
#Se debe informar al cliente si excede o no de los minutos y de cuanto es la cuenta
#A continuación 2 ejemplo de ejecución del sistema que se pide.
# ESTE ES MI COMENTARO
print("compañia telefonica")
md=int(input("ingrese la cantidad de minutos hablados por el dia: "))
mn=int(input("ingrese la cantidad de minutos hablados por la noche: "))
Tm= md-100
tmN=mn-80
tmd= (md*10)-100
tmn= (mn*7)-80
Td= (tmd+tmn)
mad=(md*15)*100
#fernancrak en la compañia telefonica 
man=(mn*13)*80 
if md<=100:
    print(f"no excede la cantidas de minutos hablados por el dia")
if mn<=80:
    print(f"no excede la cantiddad de minutos hablados por la noche")

elif md>=100:
    print(f"excede en {Tm}min por el dia, el cliente paga ${mad}")
elif mn>=80:
    print(f"excede en {tmN}min por la noche, el cliente paga ${man} ")


#el goaaaaaaaaaat siuuuuuu
