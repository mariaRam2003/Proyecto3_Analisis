# Definición de la clase MTF (Move to Front)
class MTF:
    # Constructor de la clase MTF
    def __init__(self, configuration):
        # Configuración inicial de la lista
        self.configuration = configuration

    # Método para acceder a un elemento y actualizar la configuración
    def access(self, request):
        # Costo de acceso: índice del elemento en la configuración actual
        cost = self.configuration.index(request)
        # Remover el elemento de la configuración
        self.configuration.remove(request)
        # Mover el elemento al principio de la configuración
        self.configuration.insert(0, request)
        # Devolver el costo de acceso
        return cost

# Definición de la clase IMTF (Improved Move to Front), que hereda de MTF
class IMTF(MTF):
    # Método para acceder a un elemento y actualizar la configuración (sobrescribe el método en MTF)
    def access(self, request):
        # Índice del elemento en la configuración actual
        i = self.configuration.index(request)
        # Elementos que se encuentran antes del elemento accedido en la configuración actual
        lookahead = self.configuration[:i]
        # Verificar si algún elemento posterior al accedido está en la lista de lookahead
        if any(x in lookahead for x in self.configuration[i + 1:]):
            # Si hay elementos posteriores en la lista de lookahead, mover el elemento al principio
            self.configuration.remove(request)
            self.configuration.insert(0, request)
            # Devolver el costo de acceso
            return i
        # Si no hay elementos posteriores en la lista de lookahead, el costo es 0
        return 0
    

# Función para calcular el costo total de acceso
def total_access_cost(sequence, configuration, algorithm):
    mtf = algorithm(configuration)
    total_cost = 0
    print("Configuración inicial:", configuration)
    for request in sequence:
        cost = mtf.access(request)
        total_cost += cost
        print("Solicitud:", request, "| Costo:", cost, "| Configuración:", mtf.configuration)
    print("Costo total de accesos:", total_cost)
    return total_cost

# Secuencia de solicitudes
sequence_a = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
sequence_b = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]
sequence_c = [1] * 20   
sequence_d = [3] * 20
sequence_e = [2] * 20
sequence_f = [3] * 20

# Configuración inicial
initial_configuration = [0, 1, 2, 3, 4]

# Calcular costos de acceso para MTF
print("\n--- Secuencia a (MTF) ---")
total_cost_a_mtf = total_access_cost(sequence_a, initial_configuration, MTF)

print("\n--- Secuencia b (MTF) ---")
total_cost_b_mtf = total_access_cost(sequence_b, initial_configuration, MTF)

print("\n--- Secuencia c (MTF) ---")
total_cost_c_mtf = total_access_cost(sequence_c, initial_configuration, MTF)

print("\n--- Secuencia d (MTF) ---")
total_cost_d_mtf = total_access_cost(sequence_d, initial_configuration, MTF)

print("\n--- Secuencia e (MTF) ---")
total_cost_e_mtf = total_access_cost(sequence_e, initial_configuration, MTF)

print("\n--- Secuencia f (MTF) ---")
total_cost_f_mtf = total_access_cost(sequence_f, initial_configuration, MTF)

# Calcular costos de acceso para IMTF
print("\n--- Secuencia a (IMTF) ---")
total_cost_a_imtf = total_access_cost(sequence_a, initial_configuration, IMTF)

print("\n--- Secuencia b (IMTF) ---")
total_cost_b_imtf = total_access_cost(sequence_b, initial_configuration, IMTF)

print("\n--- Secuencia c (IMTF) ---")
total_cost_c_imtf = total_access_cost(sequence_c, initial_configuration, IMTF)

print("\n--- Secuencia d (IMTF) ---")
total_cost_d_imtf = total_access_cost(sequence_d, initial_configuration, IMTF)

print("\n--- Secuencia e (IMTF) ---")
total_cost_e_imtf = total_access_cost(sequence_e, initial_configuration, IMTF)

print("\n--- Secuencia f (IMTF) ---")
total_cost_f_imtf = total_access_cost(sequence_f, initial_configuration, IMTF)