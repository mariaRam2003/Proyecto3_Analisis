class MTF:
    def __init__(self, config):
        self.config = config

    def access(self, request):
        cost = 0
        for i, item in enumerate(self.config):
            if item == request:
                cost = i + 1
                del self.config[i]
                self.config.insert(0, request)
                break
        return cost

    def total_cost(self, requests):
        total_cost = 0
        for request in requests:
            cost = self.access(request)
            total_cost += cost
            print("Configuración:", self.config)
            print("Solicitud:", request)
            print("Costo:", cost)
            print("Configuración después de MTF:", self.config)
            print("-----------------------------")
        return total_cost
