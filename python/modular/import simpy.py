import simpy
import random
import pandas as pd

# Parámetros de la simulación
RANDOM_SEED = 42
SIM_TIME = 1000  # Tiempo de simulación
INTER_ARRIVAL_TIME = 5  # Tiempo promedio entre arribos
SERVICE_TIME_E1 = 8  # Tiempo promedio de servicio en E1
SERVICE_TIME_E2 = 6  # Tiempo promedio de servicio en E2
SERVICE_TIME_E3 = 10  # Tiempo promedio de servicio en E3

# Resultados
results = []

# Función para generar el tiempo de servicio
def generate_service_time(mean_time):
    return random.expovariate(1.0 / mean_time)

# Cliente
def customer(env, name, queues, servers, results):
    arrival_time = env.now
    # Decide si ir a cola A o B
    if len(queues["A"]) <= len(queues["B"]):
        queue = "A"
        server = servers["E1"]
        service_time = generate_service_time(SERVICE_TIME_E1)
    else:
        queue = "B"
        server = servers["E2"]
        service_time = generate_service_time(SERVICE_TIME_E2)
    
    queues[queue].append(1)
    with server.request() as request:
        yield request
        # Salir de la cola y ser atendido
        queues[queue].pop(0)
        wait_time = env.now - arrival_time
        yield env.timeout(service_time)
    
    # Moverse a la cola de E3
    service_time_e3 = generate_service_time(SERVICE_TIME_E3)
    with servers["E3"].request() as request:
        yield request
        yield env.timeout(service_time_e3)
    
    # Registrar resultados
    results.append({
        "Customer": name,
        "Arrival Time": arrival_time,
        "Wait Time E1/E2": wait_time,
        "Service Time E1/E2": service_time,
        "Service Time E3": service_time_e3,
        "Total Time in System": env.now - arrival_time
    })

# Generador de clientes
def customer_generator(env, queues, servers, results):
    i = 0
    while True:
        yield env.timeout(random.expovariate(1.0 / INTER_ARRIVAL_TIME))
        env.process(customer(env, f"Customer {i}", queues, servers, results))
        i += 1

# Configuración de la simulación
random.seed(RANDOM_SEED)
env = simpy.Environment()
queues = {"A": [], "B": []}  # Longitudes de las colas
servers = {
    "E1": simpy.Resource(env, capacity=1),
    "E2": simpy.Resource(env, capacity=1),
    "E3": simpy.Resource(env, capacity=1)
}
env.process(customer_generator(env, queues, servers, results))
env.run(until=SIM_TIME)

# Convertir los resultados en DataFrame para análisis
df_results = pd.DataFrame(results)
print(df_results)
