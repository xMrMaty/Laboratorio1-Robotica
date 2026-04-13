# Laboratorio1-Robotica: 

**Equipo de Trabajo:**
* **Programador:** Matías Ruiz Flores
* **Experimentador:** Joaquín Castro Delgado
* **Analista:** Álvaro Del Pino Cerda
* **Documentador:** Matías Ruiz Flores
* **Integrador:** Joaquín Castro Delgado

**Carrera:** Ingeniería Civil Informática  
**Asignatura:** Robótica y Sistemas Autónomos (ICI 4150-2)

## Descripción del laboratorio
El objetivo de este laboratorio es comprender el comportamiento cinemático de un robot móvil diferencial mediante una simulación interactiva en Webots, donde los actuadores (motores de las ruedas) controlan el movimiento del robot.

## Cómo instalar y ejecutar la simulación en Webots
Para que Webots reconozca el entorno y el código del robot automáticamente, es fundamental mantener la estructura de archivos al descargarlos:

1. **Descargar el repositorio:** Clona este repositorio o descarga el archivo ".zip" desde GitHub. Si descargas el ".zip", **descomprímelo** en una carpeta de tu computadora (como Documentos o Escritorio).
2. **Verificar la estructura:** Asegúrate de que la carpeta extraída contenga la subcarpeta "worlds" (donde está el archivo del entorno ".wbt") y la subcarpeta "controllers" (donde está el código fuente).
3. **Abrir Webots:** Inicia el entorno de simulación de Webots.
4. **Cargar el mundo:** En el menú superior, ve a "File > Open World...". Navega hasta la carpeta que descomprimiste, entra a la carpeta "worlds" y selecciona el archivo ".wbt" (por ejemplo, "Laboratorio1.wbt").
5. **Verificar el controlador:** Haz clic en el robot e-puck en la simulación. En el panel izquierdo, despliega sus propiedades y asegúrate de que en la opción "controller" esté seleccionado el archivo "controlador_laboratorio1".
6. **Iniciar simulación:** Presiona el botón "Play" (el triángulo que apunta a la derecha) en la interfaz superior de Webots para ejecutar el código y observar los movimientos.

## Resultados obtenidos
Durante la simulación se programaron distintas velocidades para las ruedas (v_r y v_l), logrando los siguientes comportamientos:

* **¿Qué ocurre cuando ambas ruedas tienen la misma velocidad?**
* Cuando se aplica la misma velocidad a ambas ruedas, el robot se desplaza en un movimiento recto.
* **¿Cómo cambia la trayectoria cuando las velocidades son diferentes?**
* Al tener velocidades distintas, la trayectoria del robot deja de ser recta y se vuelve curva, generando un giro continuo.
* **¿Qué ocurre cuando una rueda gira en sentido opuesto a la otra?**
* Si se aplican velocidades opuestas, el robot realiza una rotación en el lugar sobre su propio eje central.
* **¿Qué tipo de movimiento permite dibujar un círculo?**
  Para dibujar un círculo se requiere aplicar y mantener velocidades diferentes en ambas ruedas de manera constante.
