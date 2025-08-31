Diccionario = {"a": "$%3", "b": "8@*", "c": "2&9", "d": "q1#", "e": "z7!",
    "f": "m$5", "g": "p@0", "h": "t^4", "i": "x&8", "j": "u*2",
    "k": "r!6", "l": "n#3", "m": "c@1", "n": "v$9", "o": "b%7",
    "p": "y^0", "q": "w&5", "r": "k*8", "s": "h!2", "t": "d#4",
    "u": "g@6", "v": "j$1", "w": "l%3", "x": "o^9", "y": "s&7",
    "z": "a*0"}

def EncriptarM(mensaje):
    Llaves = []

    for Clave in mensaje:
        ClaveMin = Clave.lower()
        if ClaveMin in Diccionario:
            Llaves.append(Diccionario[ClaveMin])
        elif Clave == " ":
            Llaves.append("<SPACE>")
        else:
            Llaves.append(Clave)
    return "|".join(Llaves)

def DesencriptarM(texto):
    Invertir = {V: k for k, V in Diccionario.items()}
    Partes = texto.split("|")
    Salida =[]

    for Llaves in Partes:
        if Llaves == "<SPACE>":
            Salida.append(" ")
        elif Llaves in Invertir:
            Salida.append(Invertir[Llaves])
        else:
            Salida.append(Llaves)
    return "".join(Salida)


if __name__ == "__main__":
    Mensaje = "Programando ando"
    Encriptar = EncriptarM(Mensaje)
    Desencriptar = DesencriptarM(Encriptar)

    print("Mensaje: ",Mensaje)
    print("======================")
    print("Encriptado: ",Encriptar)
    print("======================")
    print("Desencriptado: ",Desencriptar)