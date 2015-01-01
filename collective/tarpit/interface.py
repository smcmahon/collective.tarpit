from Products.PluggableAuthService import interfaces

class ITarpitHelper(# -*- implemented plugins -*-
                    interfaces.plugins.IAuthenticationPlugin,
                    interfaces.plugins.IExtractionPlugin,
                                ):
    """interface for TarpitHelper."""
