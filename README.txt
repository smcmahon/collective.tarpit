Introduction
============

collective.tarpit is currently an experiment.

At present, it attempts to detect failed logins and write a useful warning to syslog/auth. It should play well with fail2ban.

http basic auth is ignored. Protect it another way.

emergency-user logins via the plone login form will be incorrectly diagnosed as failed, and thus logged. This is probably a good thing.

