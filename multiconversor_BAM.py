import re # Importar módulo de expresiones regulares

# -------------------------------------------------------------
# CONSTANTES DE OPCIONES DEL MENÚ
# -------------------------------------------------------------
TEMPERATURA = 1
PESO = 2
MONEDA = 3
HISTORIAL = 4
BUSCAR = 5
SALIR = 6
# -------------------------------------------------------------
# CONSTANTES Y VARIABLES GLOBALES
# -------------------------------------------------------------
DOLAR_MXN = 18.6
EURO_USD = 1.15
EURO_MXN = 21.5
DOLAR_A_EURO = 0.87
LIBRAS = 2.20462

# -------------------------------------------------------------
# CLASE PRINCIPAL DEL PROGRAMA
# -------------------------------------------------------------
class Conversor:    # Clase para el conversor multifuncional
    def __init__(self, nombre):     # el self sirve para referirse a la instancia
        self.nombre = nombre
        self.historial = []  # Variable no primitiva (lista)
        self.tasas = {       # Variable no primitiva (diccionario)
            "dolar_mxn": DOLAR_MXN,
            "euro_usd": EURO_USD,
            "euro_mxn": EURO_MXN
        }

    def saludar(self):
        return f"\n💥💣 ¡Bienvenid@s al {self.nombre}! 💥💣\n✨ Tu compa digital que convierte TODO con estilo ✨"

    def agregar_conversion(self, descripcion):
        self.historial.append(descripcion)

    def buscar_conversion(self, termino):    
        """Filtra el historial de conversiones usando búsqueda parcial."""
        return [c for c in self.historial if termino.lower() in c.lower()]  


# -------------------------------------------------------------
# FUNCIONES AUXILIARES
# -------------------------------------------------------------
def convertir_a_minusculas(texto):
    """Convierte texto a minúsculas sin espacios."""
    return texto.lower().strip()

def validar_si_no(respuesta):
    """Usa expresiones regulares para validar respuestas de 'si' o 'no'."""
    return re.match(r'^(si|no)$', respuesta.strip().lower()) is not None


# -------------------------------------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------------------------------------
app = Conversor("Multiconversor BAM")  # Crear instancia de la clase Conversor
print(app.saludar())      # Saludo inicial
print("-" * 50)          # Separador visual

seguir = 'si'

while seguir == 'si':
    try:
        print("\n--- MENÚ PRINCIPAL --- 🌡️⚖️💰")
        print("1️⃣ Temperatura 🌡️")
        print("2️⃣ Peso ⚖️")
        print("3️⃣ Moneda 💰")
        print("4️⃣ Ver historial 📜")
        print("5️⃣ Buscar conversión 🔍")
        print("6️⃣ Salir 🚪")

        opcion = int(input("👉 ¿Qué quieres convertir hoy? "))

        # -------------------------------------------------------------
        # 1️⃣ CONVERSIONES DE TEMPERATURA
        # -------------------------------------------------------------
        if opcion == TEMPERATURA:
            print("\n🌞🔥 ¡Hora de calentar o enfriar! 🔥🌞")
            print("1️⃣ Fahrenheit ➡️ Celsius")
            print("2️⃣ Celsius ➡️ Fahrenheit")
            
            subopcion = int(input("Ingresa tu elección: "))
            valor = float(input("Ingresa el valor que quieras convertir 🌡️: "))

            if subopcion == 1: # Convertir de Fahrenheit a Celsius
                resultado = (valor - 32) * 5 / 9 
                mensaje = f"{valor:.2f} °F = {resultado:.2f} °C"   # Formateo a 2 decimales
                print(f"❄️ Resultado: {mensaje} — ¡Fresco como una lechuga! 🥬")
            elif subopcion == 2: # Convertir de Celsius a Fahrenheit
                resultado = (valor * 9 / 5) + 32
                mensaje = f"{valor:.2f} °C = {resultado:.2f} °F"      # Formateo a 2 decimales
                print(f"🔥 Resultado: {mensaje} — ¡Esto está que arde! 🔥")
            else:
                print("😅 Ups... esa opción no existe.")     
                continue

            app.agregar_conversion(f"Temperatura: {mensaje}")   # Agregar al historial

        # -------------------------------------------------------------
        # 2️⃣ CONVERSIONES DE PESO
        # -------------------------------------------------------------
        elif opcion == PESO:
            print("\n🏋️ ¡Hora de mover el cuerpo! 💪")
            print("1️⃣ Libras ➡️ Kilogramos")
            print("2️⃣ Kilogramos ➡️ Libras")

            subopcion = int(input("Ingresa tu elección: "))
            valor = float(input("Ingresa el peso que quieras convertir ⚖️: "))

            if subopcion == 1: # Convertir de Libras a Kilogramos
                resultado = valor / LIBRAS
                mensaje = f"{valor:.2f} lb = {resultado:.2f} kg"    # Formateo a 2 decimales
                print(f"💫 Resultado: {mensaje} — ¡Más livian@ de lo que pensabas! 😜")
            elif subopcion == 2:      # Convertir de Kilogramos a Libras
                resultado = valor * LIBRAS       # Multiplicamos kg por 2.20462 que es lb
                mensaje = f"{valor:.2f} kg = {resultado:.2f} lb"       # Formateo a 2 decimales
                print(f"💥 Resultado: {mensaje} — ¡Puro músculo! 💪")
            else:
                print("😅 Esa opción no está en el gimnasio.")
                continue

            app.agregar_conversion(f"Peso: {mensaje}")    # Agregar al historial

        # -------------------------------------------------------------
        # 3️⃣ CONVERSIONES DE MONEDA
        # -------------------------------------------------------------
        elif opcion == MONEDA:
            print("\n💸 ¡Hora de hablar de dinero! 💵💶💴")
            print("1️⃣ Dólares 🇺🇸 ➡️ Pesos MXN 🇲🇽")
            print("2️⃣ Pesos MXN 🇲🇽 ➡️ Dólares 🇺🇸")
            print(f"3️⃣ Dólares 🇺🇸 ➡️ Euros 🇪🇺 (Tasa fija: USD * {DOLAR_A_EURO})")
            print(f"4️⃣ Euros 🇪🇺 ➡️ Dólares 🇺🇸 (Tasa fija: {EURO_USD})")
            print(f"5️⃣ Euros 🇪🇺 ➡️ Pesos MXN 🇲🇽 (Tasa fija: {EURO_MXN})")
            print(f"6️⃣ Pesos MXN 🇲🇽 ➡️ Euros 🇪🇺 (Tasa fija: {EURO_MXN})")
            
            subopcion = int(input("Ingresa tu elección: "))
            valor = float(input("Ingresa el monto a convertir 💰: "))

            if subopcion == 1:       # Convertir de Dólares a Pesos MXN
                resultado = valor * app.tasas["dolar_mxn"]
                mensaje = f"${valor:.2f} USD = ${resultado:.2f} MXN"
            elif subopcion == 2:     # Convertir de Pesos MXN a Dólares
                resultado = valor / app.tasas["dolar_mxn"]
                mensaje = f"${valor:.2f} MXN = ${resultado:.2f} USD"
            elif subopcion == 3:     # Convertir de Dólares a Euros
                resultado = valor * 0.87
                mensaje = f"${valor:.2f} USD = €{resultado:.2f} EUR"
            elif subopcion == 4:     # Convertir de Euros a Dólares
                resultado = valor * app.tasas["euro_usd"]
                mensaje = f"€{valor:.2f} EUR = ${resultado:.2f} USD"
            elif subopcion == 5:     # Convertir de Euros a Pesos MXN  
                resultado = valor * app.tasas["euro_mxn"]
                mensaje = f"€{valor:.2f} EUR = ${resultado:.2f} MXN"
            elif subopcion == 6:    # Convertir de Pesos MXN a Euros
                resultado = valor / app.tasas["euro_mxn"]
                mensaje = f"${valor:.2f} MXN = €{resultado:.2f} EUR"
            else:
                print("😅 Opción inexistente...")
                continue

            print(f"✅ Resultado: {mensaje}")
            app.agregar_conversion(f"Moneda: {mensaje}")

        # -------------------------------------------------------------
        # 4️⃣ MOSTRAR HISTORIAL
        # -------------------------------------------------------------
        elif opcion == HISTORIAL: # Mostrar el historial de conversiones
            if app.historial:
                print("\n📜 HISTORIAL DE CONVERSIONES:")
                for h in app.historial:
                    print("•", h)
            else:
                print("🕳️ Todavía no hay conversiones registradas.")

        # -------------------------------------------------------------
        # 5️⃣ BÚSQUEDA DE CONVERSIÓN
        # -------------------------------------------------------------
        elif opcion == BUSCAR: # Buscar en el historial de conversiones
            termino = input("🔍 Ingresa un texto para buscar en el historial: ")
            resultados = app.buscar_conversion(termino) # app es la instancia de Conversor
            if resultados:
                print("\n🎯 Coincidencias encontradas:")
                for r in resultados:
                    print("•", r)
            else:
                print("😅 No se encontraron coincidencias.")

        # -------------------------------------------------------------
        # 6️⃣ SALIR
        # -------------------------------------------------------------
        elif opcion == SALIR: # Salir del programa
            seguir = 'no'
            print("\n👋 Gracias por usar el Multiconversor BAM 💥💣 ¡Vuelve pronto! 😄")

        else:
            print("😅 Esa opción no existe, prueba otra vez 💫")

        # -------------------------------------------------------------
        # PREGUNTAR SI DESEA CONTINUAR
        # -------------------------------------------------------------
        if seguir != 'no': # Si no se eligió salir
            print("-" * 50) # Separador visual
            respuesta = input("¿Quieres seguir jugando a convertir cosas? (si/no): ")
            respuesta = convertir_a_minusculas(respuesta)

            if not validar_si_no(respuesta):
                print("🙃 No entendí eso, supongo que ya te vas 🫠")
                seguir = 'no'
            else:
                seguir = respuesta

    except ValueError:
        print("❌ Error: ¡Debes ingresar un número válido o una opción numérica!")
        print("Volviendo al menú principal...")
    except Exception as e:    # e es la variable que captura el error
        print(f"Ocurrió un error inesperado: {e}")
        seguir = 'no'

# -------------------------------------------------------------
# FIN DEL PROGRAMA
# -------------------------------------------------------------
print("\n🎉 Programa terminado. ¡Eres oficialmente un/a maestr@ de las conversiones! 🏆")