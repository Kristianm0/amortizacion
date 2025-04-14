#@Kristian Martinez Colina | Programacion Python
"""Que es Amortizacion Ordinaria
El proceso de ir pagando una deuda poco a poco, en varias cuotas (mensuales, anuales, etc.), donde cada pago incluye una parte de los intereses y una parte del dinero que se pidió prestado (capital).
"""
"""Que es una tabla de amortizacion
Una tabla de amortización es una herramienta que muestra cómo vas pagando un préstamo o deuda a lo largo del tiempo. Es como un cronograma de pagos, que te dice cuánto pagas en cada período, cuánto de ese pago va para intereses, cuánto se abona al capital (la deuda original), y cuánto te queda por pagar.
"""
"""Formula para sacar cuota
Datos: 
R	Cuota fija a pagar por periodo
VP	Valor presente (el monto del préstamo)
i	Tasa de interés por periodo (ej. mensual, anual...)
n	Número total de periodos
"""

"""Que es Amortizacion con los Jovenes titanes
Amortización es como cuando Cyborg le pide dinero prestado a Robin para mejorar sus sistemas. Cyborg acuerda pagarle en cuotas mensuales. Cada pago cubre dos cosas:

Intereses: La "comisión" que Robin cobra por prestarle el dinero.

Capital: El dinero que Cyborg le devuelve, reduciendo su deuda.

Al principio, más del pago va a los intereses, pero conforme paga, más de su cuota va a reducir lo que debe, hasta que paga todo lo que le debía a Robin.
"""
"""Ejercicio con los Jovenes Titanes
Robin necesita mejorar los sistemas de defensa de la Torre de los Titanes, así que le pide prestado dinero a Cyborg.

- Monto prestado por Cyborg: $900
- Tasa de interés anual: 2%
- Plazo: 10 meses
- Tipo de pago: Cuotas fijas mensuales

Objetivo:
Calcular la cuota fija mensual que debe pagar Robin a Cyborg y elaborar una tabla de amortización con el detalle de cada pago.
"""

import pandas 

from decimal import Decimal 


def cantidad_limpia(dinero_cantidad):
    dinero_cantidad_adaptada = dinero_cantidad.replace('.', '').replace(',', '').strip()
    return Decimal(dinero_cantidad_adaptada)

def tasa_limpia(tasa):
    tasa_decimal = tasa.replace(",", ".").replace("%", "").strip()
    return Decimal(tasa_decimal) / 100

def convertir_a_dolares(valor):
    valor_formateado = f"{valor:,.2f}"  
    return f"$ {valor_formateado}"

def tabla_amortizacion():
    try: 
        valor_presente = cantidad_limpia(input("Ingresa el monto inicial: "))
        tasa_interes = input("Ingresa la tasa de interes: ")

        tipo_tiempo =  int(input(""" 
Elige un periodo de tiempo: 
1. Diaria.
2. Mensual.
3. Anual.
4. Otro periodo.
-> """))
        
        if tipo_tiempo == 1:
            tiempo_tasa_nombre = "Diaria"
            tiempo_nombre = "Dias"
            periodos_tiempo = Decimal(input("Ingresa los periodos de tiempo en dias: "))
        elif tipo_tiempo == 2: 
            tiempo_tasa_nombre = "Mensual"
            tiempo_nombre = "Meses"
            periodos_tiempo = Decimal(input("Ingresa los periodos de tiempo en meses: "))
        elif tipo_tiempo == 3: 
            tiempo_tasa_nombre = "Anual"
            tiempo_nombre = "Años"
            periodos_tiempo = Decimal(input("Ingresa los periodos de tiempo en años: "))
        elif tipo_tiempo == 4: 
            tiempo_tasa_nombre = input("Nombre del periodo: ")
            tiempo_nombre = tiempo_tasa_nombre
            periodos_tiempo = Decimal(input(f"""Ingresa los periodos de tiempo en "{tiempo_tasa_nombre}": """))
        else: 
            print("❌ Opción inválida")
            return
        
        tasa_interes_fomateada = tasa_limpia(tasa_interes)

        formula_r_cuota = valor_presente / ((1 - (1 + tasa_interes_fomateada)** - periodos_tiempo) / tasa_interes_fomateada)

        print("")
        print(f"Valor de la Cuota: {convertir_a_dolares(formula_r_cuota)} y con una tasa del {tasa_interes}% {tiempo_tasa_nombre} en un periodo de {periodos_tiempo} {tiempo_nombre} ")

        #Tabla
        deuda = valor_presente
        tabla = []
        cuota = formula_r_cuota

        for periodo in range( 1, int(periodos_tiempo) + 1):
            interes = deuda * tasa_interes_fomateada #.quantize(Decimal("0.01"))
            aporte = cuota - interes
            nueva_deuda = deuda - aporte

            tabla.append([
                periodo,
                convertir_a_dolares(deuda),
                convertir_a_dolares(cuota),
                convertir_a_dolares(interes),
                convertir_a_dolares(aporte),
                convertir_a_dolares(nueva_deuda)
            ])
            deuda = nueva_deuda
        
        df_tabla_amortizacion = pandas.DataFrame(
            tabla, 
            print("Tabla de Amortizacion"),
            columns= ["Periodo", "Deuda", "Cuota", "Interes", "Aporte", "Nueva deuda"]
        )
        print(df_tabla_amortizacion.to_string(index=False))

    except Exception as error: 
        print(f"Hubo un error {error}")

if __name__ == "__main__":
    tabla_amortizacion()




























