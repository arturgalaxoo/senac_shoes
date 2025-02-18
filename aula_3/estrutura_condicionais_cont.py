# P I Z Z A R I A S A B O R E S
# Calabresa, 4 queijos, Frango com Requeijão
# Se o cliente pedir uma pizza de calabresa na sexta-feira 
# O refri fica por conta da casa
# Se o cliente pedir qualquer pizza no sábado, o frete é grátis
# Senão, informe ao cliente apenas que a pizza solicitada está sendo preparada.

sabor_pizza = input(f"""Informe o sabor da sua pizza:
                      1- Calabresa
                      2- 4 queijos 
                      3- Frango com Requeijão
                      : """)

dia_semana = "sabado1"

if sabor_pizza == "1" and dia_semana == "sexta":
    print("Parbéns, o refri é por conta da casa.")
elif (sabor_pizza == "1" or sabor_pizza =="2" or sabor_pizza == "3")and dia_semana == "sabado":
    print("Parabéns, o frete é grátis.")
else: 
    print("A sua pizza está sendo preparada.")