class Estadistica:
    def __init__(self):
        self.ListaNum = [15,10,20,14,20,16,47,20,15,2]

    def Frecuencia(self):
        self.d = {}
        for numero in self.ListaNum:
            if numero in self.d:
                self.d[numero] += 1
            else:
                self.d[numero] = 1

        ListaTuplas = list(self.d.items())
        print("Tupla de listas:",ListaTuplas)

    def Moda(self):
        moda = max(self.d, key=self.d.get)
        print("Moda:",moda)

    def Histograma(self):
        print("Histograma")
        for key, value in self.d.items():
            print(key, ":", "*" * value)

if __name__ == "__main__":
    datos = Estadistica()
    datos.Frecuencia()
    print("================================")
    datos.Moda()
    print("================================")
    datos.Histograma()