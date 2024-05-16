# MTF
def mtf_cost(config, sequence):
    print(f"Lista de Configuración: {config}")
    print(f"Secuencia de Solicitudes: {sequence}\n")
    total_cost = 0
    for request in sequence:
        cost = config.index(request) + 1
        total_cost += cost
        config.remove(request)
        config.insert(0, request)
        print(f"Configuración: {config}, Solicitud: {request}, Costo: {cost}")
    print(f"\nCosto total: {total_cost}")
    return total_cost

def min_cost_sequence(config, lenght):
    sequence = [config[0]] * lenght
    print(f"Secuencia de Costo Mímimo encontrada: {sequence} para una longitud de {lenght} solicitudes")
    return sequence

def max_cost_sequence(config, lenght):
    sequence = []
    current_config = config[:]
    for _ in range(lenght):
        sequence.append(current_config[-1])
        current_config.insert(0, current_config.pop())  # Mueve el último elemento al frente
    print(f"Secuencia de Costo Máximo encontrada: {sequence} para una longitud de {lenght} solicitudes")
    return sequence


# IMTF
def imtf_cost(config, sequence):
    print(f"Lista de Configuración: {config}")
    print(f"Secuencia de Solicitudes: {sequence}\n")
    total_cost = 0
    n = len(sequence)
    for i, request in enumerate(sequence):
        cost = config.index(request) + 1
        total_cost += cost
        
        # Look-ahead para decidir si mover el elemento al frente
        if request in sequence[i+1:i+cost]:
            config.remove(request)
            config.insert(0, request)
        
        print(f"Configuración: {config}, Solicitud: {request}, Costo: {cost}")
    print(f"\nCosto total: {total_cost}")
    return total_cost


# Preguntas
# ----- A -----
print("\n","-"*10,"Pregunta A","-"*10)
config_a = [0, 1, 2, 3, 4]
sequence_a = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
cost_a = mtf_cost(config_a, sequence_a)

# ----- B -----
print("\n\n","-"*10,"Pregunta B","-"*10)
config_b = [0, 1, 2, 3, 4]
sequence_b= [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]
cost_b = mtf_cost(config_b, sequence_b)

# ----- C -----
print("\n\n","-"*10,"Pregunta C","-"*10)
config_c = [0, 1, 2, 3, 4]
sequence_c = min_cost_sequence(config_c, 20)
print("")
cost_c = mtf_cost(config_c, sequence_c)

# ----- D -----
print("\n\n","-"*10,"Pregunta D","-"*10)
config_d = [0, 1, 2, 3, 4]
sequence_d = max_cost_sequence(config_d, 20)
print("")
cost_d = mtf_cost(config_d, sequence_d)

# ----- E -----
print("\n\n","-"*10,"Pregunta E","-"*10)
config_e1 = [0, 1, 2, 3, 4]
sequence_e1 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
print("")
cost_e1 = mtf_cost(config_e1, sequence_e1)
print("\n")
config_e2 = [0, 1, 2, 3, 4]
sequence_e2 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
print("")
cost_e2 = mtf_cost(config_e2, sequence_e2)

# ----- F -----
print("\n\n","-"*10,"Pregunta F","-"*10)
config_f1 = [0, 1, 2, 3, 4]
n_1 = 20
print("Secuencia de Costo Mínimo (IMTF)")
best_sequence = min_cost_sequence(config_f1, n_1)
print("")
cost_f1 = imtf_cost(config_f1, best_sequence)
print("\n")
config_f2 = [0, 1, 2, 3, 4]
n_2 = 20
print("Secuencia de Costo Máximo (IMTF)")
worst_sequence = max_cost_sequence(config_f2, n_2)
print("")
cost_f2 = imtf_cost(config_f2, worst_sequence)   