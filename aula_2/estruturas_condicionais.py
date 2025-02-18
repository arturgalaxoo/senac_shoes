# No Brasil, para alguém dirigir a pessoa precisa de 18 anos.
# Se a pessoa tiver a partir de 18 anos, pode drigir.
# Se ela tiver entre 0 até 17 anos, não pode dirigir
# Senão, informe uma idade válida

#if idade_pessoa >= 18:
#
#elif idade_pessoa  >= 0 and idade_pessoa <= 17:
#    print("Você não pode dirigir :(")
#else:
#    print("Informe uma idade válida")


# Condicional aninhada
idade = 19
habilitacao = False

if idade >= 18:
    if habilitacao == True:
        print("Você pode dirigir!")
    else:
        print("Você não possui habilitação")
else: 
    print("Você não tem idade suficiente para dirigir!")

