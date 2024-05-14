def mtf_cost(config, sequence):
    cost_total = 0
    config_list = config[:]
    for req in sequence:
        cost = config_list.index(req) + 1
        cost_total += cost
        config_list.remove(req)
        config_list.insert(0, req)
        print(f"Configuración de lista: {config_list}, Solicitud: {req}, Costo: {cost}")
    return cost_total

def best_case_mtf(config, length):
    return config * (length // len(config))

def worst_case_mtf(config, length):
    seq = []
    while len(seq) < length:
        for i in reversed(config):
            if len(seq) < length:
                seq.append(i)
    return seq

def imtf_cost(config, sequence):
    cost_total = 0
    config_list = config[:]
    for req in sequence:
        cost = config_list.index(req) + 1
        cost_total += cost
        if req in config_list[:cost-1]:
            config_list.remove(req)
            config_list.insert(0, req)
        print(f"Configuración de lista: {config_list}, Solicitud: {req}, Costo: {cost}")
    return cost_total

# Parte a
print("Parte a")
config_a = [0, 1, 2, 3, 4]
sequence_a = [0, 1, 2, 3, 4] * 4
total_cost_a = mtf_cost(config_a, sequence_a)
print(f"Costo total de acceso (a): {total_cost_a}\n")

# Parte b
print("Parte b")
config_b = [0, 1, 2, 3, 4]
sequence_b = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]
total_cost_b = mtf_cost(config_b, sequence_b)
print(f"Costo total de acceso (b): {total_cost_b}\n")

# Parte c
print("Parte c")
best_sequence = best_case_mtf(config_a, 20)
print(f"Mejor secuencia: {best_sequence}")
total_cost_best = mtf_cost(config_a, best_sequence)
print(f"Costo total de acceso (mejor caso): {total_cost_best}\n")

# Parte d
print("Parte d")
worst_sequence = worst_case_mtf(config_a, 20)
print(f"Peor secuencia: {worst_sequence}")
total_cost_worst = mtf_cost(config_a, worst_sequence)
print(f"Costo total de acceso (peor caso): {total_cost_worst}\n")

# Parte e
print("Parte e")
sequence_e1 = [2] * 20
sequence_e2 = [3] * 20
total_cost_e1 = mtf_cost(config_a, sequence_e1)
total_cost_e2 = mtf_cost(config_a, sequence_e2)
print(f"Costo total de acceso (2 repetido): {total_cost_e1}")
print(f"Costo total de acceso (3 repetido): {total_cost_e2}\n")

# Parte f
print("Parte f")
print("IMTF Mejor caso")
total_cost_imtf_best = imtf_cost(config_a, best_sequence)
print(f"Costo total de acceso IMTF (mejor caso): {total_cost_imtf_best}\n")

print("IMTF Peor caso")
total_cost_imtf_worst = imtf_cost(config_a, worst_sequence)
print(f"Costo total de acceso IMTF (peor caso): {total_cost_imtf_worst}\n")
