def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) com base no peso (em kg) e altura (em metros).
    Retorna o valor do IMC.
    """
    return peso / (altura ** 2)

def interpretar_imc(imc):
    """
    Interpreta o Índice de Massa Corporal (IMC) e retorna uma mensagem correspondente.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em metros: "))

    imc = calcular_imc(peso, altura)
    print("Seu IMC é:", imc)
    print("Interpretação:", interpretar_imc(imc))

if __name__ == "__main__":
    main()