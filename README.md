# Laboratorio1-Robotica

**Programador:** Matías Ruiz Flores
**Experimentador:** Joaquín Castro Delgado
**Analista:** Álvaro Del Pino Cerda
**Documentador:** Matías Ruiz Flores
**Integrador:** Joaquín Castro Delgado
**Carrera:** Ingeniería Civil Informática
**Asignatura:** Robótica y Sistemas Autónomos (ICI 4150-2)

## Descripción del laboratorio
El objetivo de este laboratorio es comprender el comportamiento cinemático de un robot móvil diferencial mediante una simulación interactiva en Webots, donde los actuadores (motores de las ruedas) controlan el movimiento del robot.

## Cómo ejecutar la simulación en Webots
1. Clonar o descargar este repositorio.
2. Abrir el entorno de Webots.
3. Ir a File > Open World... y seleccionar el archivo del mundo virtual asociado a este laboratorio.
4. Asegurarse de que el controlador del robot e-puck esté asignado a controlador_laboratorio1.py.
5. Presionar el botón "Play" en la interfaz superior de Webots para iniciar la simulación.

## Resultados obtenidos
Durante la simulación se programaron distintas velocidades para las ruedas (v_r y v_l), logrando los siguientes comportamientos:

1. **¿Qué ocurre cuando ambas ruedas tienen la misma velocidad?**
Cuando se aplica la misma velocidad a ambas ruedas, el robot se desplaza en un movimiento recto.
2. **¿Cómo cambia la trayectoria cuando las velocidades son diferentes?**
Al tener velocidades distintas, la trayectoria del robot deja de ser recta y se vuelve curva, generando un giro continuo.
3. **¿Qué ocurre cuando una rueda gira en sentido opuesto a la otra?**
Si se aplican velocidades opuestas, el robot realiza una rotación en el lugar sobre su propio eje central.
4. **¿Qué tipo de movimiento permite dibujar un círculo?**
Para dibujar un círculo se requiere aplicar y mantener velocidades diferentes en ambas ruedas de manera constante.
