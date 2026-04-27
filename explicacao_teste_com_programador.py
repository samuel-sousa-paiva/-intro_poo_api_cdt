class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.bateria = 100

    def fazer_chamada(self, custo_bateria):
        print(f"\n--- Chamada no {self.modelo} ---")

        try:
            self.bateria -= int(custo_bateria)

        except TypeError:
            print("Erro: O custo da bateria deve ser um número!")

        except ValueError:
            print("Erro: Digite um número válido!")

        else:
            print(f"Sucesso! Bateria atual: {self.bateria}%")

        finally:
            print("Sistema finalizado.")


celular = Celular("Samsung", "S24")
celular.fazer_chamada(10)