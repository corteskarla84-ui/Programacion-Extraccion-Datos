# Cortes Fregoso Karla Stephanie | Grupo: 951 | Fecha: 01/11/25

import pandas as pd

def crear_dataframe():
    datos = {
        'Tienda': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
        'Producto': ['Manzana', 'Platano', 'Naranja', 'Manzana', 'Platano', 'Naranja', 'Manzana', 'Platano', 'Naranja'],
        'Categoria': ['Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta'],
        'Precio': [30, 20, 35, 25, 30, 45, 35, 20, 25],
        'Cantidad Vendida': [50, 30, 20, 60, 25, 35, 55, 20, 30],
        'Calificacion': ['A', 'B', 'C', 'A', 'B', 'A', 'C', 'B', 'A']
    }

    df = pd.DataFrame(datos)
    print("=== DATAFRAME ORIGINAL ===")
    print(df)
    print("\n")
    return df


def Asignar_codigos(df):
    print("=== ASIGNAR CODIGOS ===")

    # Mapeo tiendas
    mapeo_tiendas = {'A': 1, 'B': 2, 'C': 3}
    df['Codigo Tienda'] = df['Tienda'].map(mapeo_tiendas)

    # Mapeo calificaciones
    mapeo_calificaciones = {'A': 3, 'B': 2, 'C': 1}
    df['Calificacion Numerica'] = df['Calificacion'].map(mapeo_calificaciones)

    print("DataFrame con codigos asignados:")
    print(df)
    print("\n")
    return df


def Total_ventas_tienda(df):
    print("=== TOTAL VENTAS POR TIENDA ===")

    # Total de ventas por fila
    df['Total Venta'] = df['Precio'] * df['Cantidad Vendida']

    # Agrupamos por tienda y sumamos
    ventas_tienda = df.groupby('Tienda')['Total Venta'].sum()

    print("Total de ventas por tienda:")
    print(ventas_tienda)
    print("\n")
    return ventas_tienda


def Precio_promedio(df):
    print("=== PRECIO PROMEDIO POR TIENDA ===")

    precio_promedio = df.groupby('Tienda')['Precio'].mean()

    print("Precio promedio por tienda:")
    print(precio_promedio.round(2))
    print("\n")
    return precio_promedio


def Cantidad_vendida(df):
    print("=== CANTIDAD VENDIDA ===")

    tabla_pivot = pd.pivot_table(
        df,
        values='Cantidad Vendida',
        index='Producto',
        columns='Tienda',
        aggfunc='sum',
        fill_value=0
    )

    print("Cantidad vendida por producto y tienda:")
    print(tabla_pivot)
    print("\n")
    return tabla_pivot


def Total_ventas(df):
    print("=== TOTAL VENTAS ===")

    if 'Total Venta' not in df.columns:
        df['Total Venta'] = df['Precio'] * df['Cantidad Vendida']

    tabla_ventas = pd.pivot_table(
        df,
        values='Total Venta',
        index='Producto',
        columns='Tienda',
        aggfunc='sum',
        fill_value=0
    )

    print("Total de ventas por producto y tienda:")
    print(tabla_ventas)
    print("\n")
    return tabla_ventas


if __name__ == "__main__":
    df = crear_dataframe()
    Asignar_codigos(df)
    Total_ventas_tienda(df)
    Precio_promedio(df)
    Cantidad_vendida(df)
    Total_ventas(df)

