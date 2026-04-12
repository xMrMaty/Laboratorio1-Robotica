from controller import Robot

# 1. Inicializar el robot
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# 2. Identificar los motores de las ruedas izquierda y derecha [cite: 37]
# El robot se controla mediante dos motores [cite: 23]
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Configurar los motores para que giren infinitamente (modo control de velocidad)
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Empezar con velocidad 0
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Temporizador para cambiar de movimiento
tiempo_actual = 0.0

# 3. Programar el robot para controlar las velocidades de las ruedas [cite: 38]
while robot.step(timestep) != -1:
    tiempo_actual += timestep / 1000.0

    # Experimento 1: Movimiento recto [cite: 40, 47]
    # Ocurre cuando vr = vl 
    if tiempo_actual < 4.0:
        left_motor.setVelocity(3.0)
        right_motor.setVelocity(3.0)

    # Experimento 2: Trayectoria curva / Círculo [cite: 41, 59, 60]
    # Ocurre cuando vr != vl [cite: 41]
    elif tiempo_actual < 12.0:
        left_motor.setVelocity(2.0)
        right_motor.setVelocity(5.0)

    # Experimento 3: Rotación en el lugar [cite: 42, 49]
    # Ocurre cuando vr = -vl 
    elif tiempo_actual < 16.0:
        left_motor.setVelocity(-3.0)
        right_motor.setVelocity(3.0)

    # Detener el robot al finalizar
    else:
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)