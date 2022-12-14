import zope.interface

class IStatus(zope.interface.Interface):

    def get_status(self):
        pass


