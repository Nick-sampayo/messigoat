class Veiculos:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
    
    def frear(self):
        print(f"O {self.modelo} está desacelerando")

    def acelerar(self):
        print(f"O {self.modelo} está acelerando")

    def porta(self):
        print(f"O {self.modelo} abriu a porta")
    
class Moto(Veiculos):
    def __init__(self, marca, modelo, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada

    def empinar(self):
        print(f"A {self.modelo} está empinando")
    
if __name__ == "__main__":
    veiculo1 = Veiculos("Caoa_Cherry", "Tiggo_5", "Preto")
    print(veiculo1.marca, veiculo1.modelo, veiculo1.cor)
    
    moto1 = Moto("Honda", "PCX", "160cc")
    print(moto1.marca, moto1.modelo, moto1.cilindrada)
    
    veiculo1.frear()
    veiculo1.acelerar()
    veiculo1.porta()
    moto1.empinar()
                    