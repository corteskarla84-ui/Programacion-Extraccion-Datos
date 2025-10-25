# Cortes Fregoso Karla Stephanie | Grupo: 951 | Fecha: 25/10/25
import pandas as pd
import numpy as np

def crear_nulos():
    Datos = {
        "IDCliente": [np.nan, 102, 103, 101, 104, np.nan, 102, 106, 107, 103, 108, 109, 101, 110],
        "Nombre": ["Ana", np.nan, "Panfilo", "Ana", "Panfilo", np.nan, "Luis", "Elena", np.nan, "Maria", np.nan, "Carlos", "Ana", "David"],
        "CategoriaProducto": [np.nan, "Ropa", "Hogar", "Electronicos", np.nan, "Juguetes", "Ropa", np.nan, "Electronicos", "Ropa", "Deportes", "Juguetes", "Electronicos", "Libros"],
        "Precio": [300, 100, np.nan, 300, 90, 200, 50, 75, np.nan, 120, 90, 900, 300, 200],
        "MetodoPago": ["Tarjeta", np.nan, "Transferencia", "Efectivo", "Tarjeta", np.nan, np.nan, "Efectivo", "Tarjeta", "PayPal", "Transferencia", "Efectivo", "Tarjeta", "Tarjeta"],
        "Descuento": [10, 5, 5, np.nan, 15, 0, np.nan, 0, 12, 10, 15, 12, 10, np.nan]
    }

    df = pd.DataFrame(Datos)
    return df


def PorcentajeNulos(df: pd.DataFrame):
    porcentaje = (df.isnull().mean() * 100).round(2)

    print("Porcentaje de valores nulos por columna:")
    for col, pct in porcentaje.items():
        print(f"   {col}: {pct}%")
    return porcentaje


def ReglonesDuplicados(df: pd.DataFrame):
    duplicados = df.duplicated().sum()
    print(f"Numero de renglones duplicados: {duplicados}")
    return duplicados


def ColumnasEliminadas(df: pd.DataFrame, MaxPorcentaje):
    if not (0 <= MaxPorcentaje <= 1):
        raise ValueError("El porcentaje maximo debe estar entre 0 y 1")

    #Porcentaje nulos
    PorNulos = df.isnull().mean()

    #Columnas a eliminar, no cumplen con condicion
    ColumnasEliminar = PorNulos[PorNulos >= MaxPorcentaje].index.tolist()

    #Eliminar columnas del df
    if ColumnasEliminar:
        df.drop(columns=ColumnasEliminar, inplace=False)
        print(f"Columnas eliminadas: {ColumnasEliminar}")
    else:
        print("No se eliminaron columnas")
    return ColumnasEliminar


def SustituirNulos(df: pd.DataFrame, columnas: list, metodo: str):
    if metodo not in ["mean", "bfill", "ffill"]:
        raise ValueError("El metodo debe ser: mean, bfill o ffill")

    #Crear copia
    df_resultado = df.copy()

    for col in columnas:
        if col in df_resultado.columns:
            try:
                if metodo == 'mean':
                    #Verificar si la columna es numerica
                    if pd.api.types.is_numeric_dtype(df_resultado[col]):
                        df_resultado[col] = df_resultado[col].fillna(df_resultado[col].mean())
                        print(f"{col}: nulos sustituidos con la media ({df_resultado[col].mean()})")
                    else:
                        print(f"{col}: no es numerica")
                else:
                    df_resultado[col] = df_resultado[col].fillna(method=metodo)
                    print(f"{col}: nulos sustituidos con {metodo}")
            except Exception as e:
                print(f"Error en columna {col}: {e}")
        else:
            print(f"La columna {col} no existe en el DataFrame")

    return df_resultado


def EliminarRenglones(df: pd.DataFrame):
    antes = len(df)
    df.drop_duplicates(inplace=True)
    despues = len(df)
    eliminados = antes - despues
    print(f"Renglones eliminados: {eliminados}")
    print(f"Filas antes: {antes}, filas despues: {despues}")
    return eliminados

def EstadoDataframe(df: pd.DataFrame, titulo: str):
    print(f"{titulo}")
    print(f"Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")
    print(f"Valores nulos totales: {df.isnull().sum().sum()}")
    print(f"Duplicados: {df.duplicated().sum()}")



if __name__ == "__main__":
    dfOriginal = crear_nulos()
    # Copia
    df = dfOriginal.copy()
    EstadoDataframe(df, "=== DATAFRAME ORIGINAL ===")
    print(df.head())

    print("\n======== Porcentaje de Valores Nulos ========")
    PorcentajeNulos(df)

    print("\n======== Numero de Renglones Duplicados ========")
    ReglonesDuplicados(df)

    print("\n======== Lista de Columnas Eliminadas ========")
    # Eliminar columnas con nulos (ejemplo: 30%)
    ColumnasEliminadas(df,0.20)
    EstadoDataframe(df, "=== DESPUES DE ELIMINAR COLUMNAS ===")

    print("\n======== Sustitucion de Valores Nulos ========")
    columnasNumericas = df.select_dtypes(include=[np.number]).columns.tolist()
    df_limpio = SustituirNulos(df, columnasNumericas, "mean")
    EstadoDataframe(df_limpio, "=== DESPUES DE SUSTITUIR NULOS ===")

    print("\n======== Eliminacion de Renglones Duplicados ========")
    eliminados = EliminarRenglones(df_limpio)
    EstadoDataframe(df_limpio, "=== DATAFRAME FINAL ===")
    print(df_limpio)

