from AccessControl.SecurityInfo import ClassSecurityInfo
from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin

import inspect

import logging
import logging.handlers

logger = logging.getLogger("collective.tarpit")
hdlr = logging.handlers.SysLogHandler(
        address="/dev/log",
        facility=logging.handlers.SysLogHandler.LOG_AUTH,
        )
formatter = logging.Formatter('plone: %(levelname)s: %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)


class AuthenticationPlugin(BasePlugin):
    """ Map credentials to a user ID.
    """
    security = ClassSecurityInfo()

    security.declarePrivate('authenticateCredentials')

    def authenticateCredentials(self, credentials):

        """
          Log failed authentications.

          Note that logins via the emergency user will be incorrectly
          diagnosed as failures. For that reason, we're going to ignore
          basic_auth, which is hopefully otherwise protected.

          This plugin needs to be last in the authentication chain so
          that it can check to see if the user is already authenticated.
        """

        if credentials['extractor'] == 'credentials_basic_auth':
            return None

        # examine the calling function's locals to see if there
        # is a sign that a previous authentication plugin has
        # handled this attempt.
        authd_user_ids = inspect.stack()[1][0].f_locals['user_ids']
        if not authd_user_ids:
            environ = self.REQUEST.environ
            # let's not send any non-ascii to the log
            login = credentials['login'].decode('utf8', 'replace').encode('ASCII', 'replace')
            message = 'Failed password for user "%s" site %s from %s' % (
                login,
                '/'.join(self.getPhysicalPath()[:-2]),
                environ.get(
                    'X-Forwarded-For',
                    environ.get('REMOTE_ADDR', 'NO REMOTE ADDRESS')
                    )
            )
            logger.warning(message)

        return None

