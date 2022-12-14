import zope.interface

class IActHandler(zope.interface.Interface):

    def act(self):
        pass
