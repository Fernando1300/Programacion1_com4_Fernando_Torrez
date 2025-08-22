# Calculadora de propinas en un restaurante 

# Un restaurante quiere ayudar a sus clientes a calcular cuánto dejar de propina según el monto de la cuenta. 

#Ingreso el monto de la cuenta y y lo guardamos como número decimal (float)
monto = float(input("Ingrese el monto toatal de la cuenta: "))

#Calculo la propina al 10% y 15% del monto
propina_10 = monto * 0.10
propina_15 = monto * 0.15

#Sumo la propina del 10% y el 15% al monto original para saber el total a pagar
total_a_pagar_10 = monto + propina_10
total_a_pagar_15 = monto + propina_15

#Muestro en pantalla el valor de la propina sugerida al 10% 
print("Propina sugerida (10%): ",propina_10 )

#Muestro en pantalla el total a pagar con la propina del 10% incluida
print("Total a pagar (10%): ",total_a_pagar_10 ) 

#Muestro en pantalla el valor de la propina sugerida al 15%
print("Propina sugerida (15%): ",propina_15)

#Muestro en pantalla el total a pagar con la propina del 15% incluida
print("Total a pagar (15%): ",total_a_pagar_15)