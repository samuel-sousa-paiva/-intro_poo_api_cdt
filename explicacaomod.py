def aula_tratamento_erros():
    print("--- Desafio ---")
    try:
        numerador = int(input("Digite o numerador: "))
        denominador = int(input("Digite o denominador: "))

        resultado = numerador / denominador
        print(f"Resultado: {resultado}")

    except ValueError:
        print("Erro: Digite apenas números inteiros!")

    except ZeroDivisionError:
        print("Erro: não pode dividir por zero.")

    except Exception as erro:
        print(f"Erro inesperado: {erro}")

    finally:
        print("--- Fim da divisão ---")


aula_tratamento_erros()