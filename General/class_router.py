class Router:
    def __init__(self, model, swversion, ip_add, description):
        self.model = model
        self.swversion = swversion
        self.ip_add = ip_add
        self.description = description

    # Deze methode hoort BINNEN de klasse (ingesprongen!)
    def getdescp(self):
        desc = f' router model                   : {self.model}\n'\
               f' software version               : {self.swversion}\n'\
               f' router mgmt address            : {self.ip_add}\n'\
               f' description                    : {self.description}\n'
        return desc  # Geef de variabele 'desc' terug!


# Maak nu pas de instanties (objecten) aan
rtr1 = Router('iosv', '15.6.7', '10.10.10.10', 'virtual router')
rtr2 = Router('iosv', '15.6.7', '10.10.10.11', 'virtual router')


class Switch(Router):
        def getdescp(self):
            desc = f' switch model                      : {self.model}\n'\
               f' software version                      : {self.swversion}\n'\
               f' router mgmt address                   : {self.ip_add}\n'\
               f' description                           : {self.description}\n'
            return desc  # Geef de variabele 'desc' terug!

sw1 = Switch('iosv', '15.6.7', '10.10.10.11', 'virtual router')


# Zo roep je de nieuwe methode aan:
print (rtr1.getdescp())
print (rtr2.getdescp())
print (sw1.getdescp())
