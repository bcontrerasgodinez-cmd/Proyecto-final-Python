Multiconversor BAM
📘 Descripción del programa
El Multiconversor BAM es un programa interactivo desarrollado en Python que permite realizar diferentes tipos de conversiones desde la consola.
Incluye conversiones de:
🌡️ Temperatura
⚖️ Peso
💰 Moneda
El programa también mantiene un historial de conversiones y ofrece una función de búsqueda para localizar conversiones anteriores mediante coincidencias parciales.
Además, cuenta con validación de entradas y manejo de errores para evitar fallos durante su ejecución.
▶️ Instrucciones de uso
1. Asegúrate de tener Python 3 instalado en tu computadora.
2. Ejecuta el archivo principal
3. En el menú principal, selecciona una opción ingresando el número correspondiente:
   1: Conversión de temperatura
   2: Conversión de peso
   3: Conversión de moneda
   4: Ver historial de conversiones
   5: Buscar en el historial
   6: Salir del programa
4. Sigue las instrucciones que el programa mostrará en pantalla para realizar la conversión deseada.
5. Al finalizar cada conversión, podrás decidir si deseas continuar o salir.

Documentación técnica básica

  Estructura principal
  
  El programa está compuesto por:
   
   -Constantes: Representan las opciones del menú y las tasas de conversión.
  
Clase Conversor:
Maneja el nombre del programa.
  
  -Almacena el historial de conversiones.
   
  -Contiene métodos para saludar, registrar conversiones y buscar resultados en el historial.
    
Funciones auxiliares:
  
  -convertir_a_minusculas(texto)
  
  -validar_si_no(respuesta) (usa expresiones regulares)
  
Bucle principal:
  
  -Controla el menú.
  
  -Maneja cada tipo de conversión.
  
Conversión de temperatura

  -Fahrenheit ➡ Celsius
  
  -Celsius ➡ Fahrenheit
  
Conversión de peso

  -Libras ↔ Kilogramos
  
Conversión de moneda

  -USD ↔ MXN
  
  -USD ↔ EUR
  
  -EUR ↔ MXN
  
Historial

  -Cada conversión realizada se almacena en una lista dentro de la clase Conversor.
  
Búsqueda

  -Utiliza coincidencias parciales minúscula-insensible para encontrar entradas en el historial.
  
Validaciones

  -Entradas numéricas
  
  -Opciones de menú
  
  -Respuestas “si/no” con expresiones regulares
  
Manejo de errores

  -except ValueError:
  
  -except Exception as e:

  -Controla errores usando try-except.


Gracias por usar el Multiconversor BAM!!!   




