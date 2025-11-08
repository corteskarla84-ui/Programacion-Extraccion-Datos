# Cortes Fregoso Karla Stephanie | Grupo: 951 | Fecha: 07/11/25
# Meta 3.2
import pandas as pd
import numpy as np


def crear_dataframe():
    np.random.seed(42) # Para que los numeros aleatorios sean siempre los mismos

    datos = {
        'A': np.random.randint(100, 1000, 3),
        'B': np.random.randint(100, 1000, 3),
        'C': np.random.randint(100, 1000, 3)
    }

    ventas = pd.DataFrame(datos, index=['Enero', 'Febrero', 'Marzo'])
    print("=== DATAFRAME DE VENTAS ORIGINAL ===")
    print(ventas)
    print("\n")
    return ventas


def seleccionar_loc(df, filas=None, columnas=None):
    print("=== SELECCION DE DATOS CON LOC ===")

    try:
        if filas is not None and columnas is not None:
            resultado = df.loc[filas, columnas]
            print(f"Filas: {filas}, Columnas: {columnas}")
        elif filas is not None:
            resultado = df.loc[filas]
            print(f"Filas: {filas}, Todas las columnas")
        elif columnas is not None:
            resultado = df.loc[:, columnas]
            print(f"Todas las filas, Columnas: {columnas}")
        else:
            resultado = df.copy()
            print("DataFrame completo")

        print("Resultado:")
        print(resultado)
        print("\n")
        return resultado

    except Exception as e:
        print(f"Error en selección loc: {e}")
        return None


def seleccionar_iloc(df, filas=None, columnas=None):
    print("=== SELECCION DE DATOS CON ILOC ===")

    try:
        if filas is not None and columnas is not None:
            resultado = df.iloc[filas, columnas]
            print(f"Posiciones filas: {filas}, Posiciones columnas: {columnas}")
        elif filas is not None:
            resultado = df.iloc[filas]
            print(f"Posiciones filas: {filas}, Todas las columnas")
        elif columnas is not None:
            resultado = df.iloc[:, columnas]
            print(f"Todas las filas, Posiciones columnas: {columnas}")
        else:
            resultado = df.copy()
            print("DataFrame completo")

        print("Resultado:")
        print(resultado)
        print("\n")
        return resultado

    except Exception as e:
        print(f"Error en: {e}")
        return None


def modificar_venta(df, producto, mes, nuevo_valor):
    print("=== MODIFICACION DE VENTAS ===")

    try:
        print(f"Antes de modificar - {producto} en {mes}: {df.loc[mes, producto]}")

        # Modificar usando loc
        df.loc[mes, producto] = nuevo_valor

        print(f"Despues de modificar - {producto} en {mes}: {df.loc[mes, producto]}")
        print("DataFrame actualizado:")
        print(df)
        print("\n")
        return df

    except Exception as e:
        print(f"Error al modificar: {e}")
        return df


def mostrar_estadisticas(df):
    print("=== ESTADISTICAS DEL DATAFRAME ===")
    print(f"Ventas totales por producto:")
    print(df.sum())
    print(f"\nVentas promedio por producto:")
    print(df.mean().round(2))
    print(f"\nVentas maximas por producto:")
    print(df.max())
    print(f"\nVentas minimas por producto:")
    print(df.min())
    print("\n")


if __name__ == "__main__":
    ventas_df = crear_dataframe()
    # Ventas del producto A en enero
    seleccionar_loc(ventas_df, filas='Enero', columnas='A')
    # Ventas de todos los productos en febrero
    seleccionar_loc(ventas_df, filas='Febrero')
    # Ventas de todos los productos en enero y marzo
    seleccionar_loc(ventas_df, filas=['Enero', 'Marzo'])

    # Ventas del primer mes para todos los productos
    seleccionar_iloc(ventas_df, filas=0)
    # Ventas del segundo producto en todos los meses
    seleccionar_iloc(ventas_df, columnas=1)
    # Ventas del segundo y tercer mes para el primer producto
    seleccionar_iloc(ventas_df, filas=[1, 2], columnas=0)

    # Cambiar valor del producto B en marzo a 1200
    ventas_df = modificar_venta(ventas_df, 'B', 'Marzo', 1200)
    mostrar_estadisticas(ventas_df)
