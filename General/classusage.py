class Router:
    """Router class"""
    def __init__(self, model, swversion, ip_add):
        """init values"""
        self.model = model
        self.swversion = swversion
        self.ip_add = ip_add

    def getdesc(self):
        desc= f'router model:              {self.model}\n'\
          f'router version:            {self.swversion}\n'\
          f'router IP address:         {self.ip_add}\n'
        return desc
class Switch(Router):
    def getdesc(self):
        desc= f'switch model:              {self.model}\n'\
          f'switch version:            {self.swversion}\n'\
          f'switch IP address:         {self.ip_add}\n'
        return desc



