import importlib

class Service:
    def __init__(self):
        pass

    def execute(self, service_name, method, params):
        service = importlib.import_module('services.'+service_name )
        return getattr(service.Main(), method)(params)
