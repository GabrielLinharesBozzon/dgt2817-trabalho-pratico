def soma(numero1, numero2):
    return numero1 + numero2


def subtracao(numero1, numero2):
    return numero1 - numero2


def multiplicacao(numero1, numero2):
    return numero1 * numero2


def divisao(numero1, numero2):
    if numero2 == 0:
        return "Não foi possível realizar a divisão por 0"
    return numero1 / numero2


def calculadora(numero1, numero2, operacao):
    operacao = operacao.strip().lower()
    if operacao in ("+", "soma"):
        return soma(numero1, numero2)
    if operacao in ("-", "subtracao", "subtração"):
        return subtracao(numero1, numero2)
    if operacao in ("*", "x", "multiplicacao", "multiplicação"):
        return multiplicacao(numero1, numero2)
    if operacao in ("/", "divisao", "divisão"):
        return divisao(numero1, numero2)
    return "Operação inválida"


def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Entrada inválida. Digite um número.")


saida = "s"
while saida.strip().lower() != "n":
    primeiro = ler_numero("Digite o primeiro número: ")
    segundo = ler_numero("Digite o segundo número: ")
    operacao = input("Operação (+, -, *, / ou nome): ")
    resultado = calculadora(primeiro, segundo, operacao)
    if isinstance(resultado, float) and resultado.is_integer():
        resultado = int(resultado)
    print("Resultado da operação: " + str(resultado))
    saida = input("Deseja continuar? (S/N): ")
    while saida.strip().lower() not in ("s", "n"):
        saida = input("Resposta inválida. Digite S para continuar ou N para sair: ")

print("Programa encerrado.")
