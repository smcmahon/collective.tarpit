from AccessControl.SecurityInfo import ClassSecurityInfo

from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin


class ExtractionPlugin(BasePlugin):
    """Extracts login name and credentials from a request.
    """
    security = ClassSecurityInfo()

    security.declarePrivate('extractCredentials')
    def extractCredentials(self, request):
        """request -> {...}

        o Return a mapping of any derived credentials.

        o Return an empty mapping to indicate that the plugin found no
          appropriate credentials.
        """
        creds = {}

        if getattr(request, '__ac_password'):
            print "XXX ran extractCredentials"

        return creds
