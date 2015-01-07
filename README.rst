Introduction
============

collective.tarpit is currently an experiment.

At present, it attempts to detect failed logins and write a useful warning to syslog/auth. It should play well with fail2ban.

http basic auth is ignored. Protect it another way.

emergency-user logins via the plone login form will be incorrectly diagnosed as failed, and thus logged. This is probably a good thing.

Use with a reverse proxy
------------------------

If you use a reverse-proxy for rewriting and/or caching, the IP address making the Zope/Plone request will be that of the proxy -- typically 127.0.0.1. This is not useful information. collective.tarpit instead checks first for the X-Real-IP header, which should be set by your reverse proxy to the requesting IP. If X-Real-IP is not available, X-Forwarded-For is checked, that the first address listed is considered the request source.

Finally, if neither X-Real-IP nor X-Forwarded-For is present, the immediately requesting IP will be reported.

This means that you need to configure your outermost reverse-proxy to set X-Real-IP. In Nginx, this is done with the directive::

    proxy_set_header X-Real-IP $remote_addr;

Most or all reverse proxies, including Apache, will have a similar facility, or do this automatically.

Use with fail2ban
-----------------

collective.tarpit may be used in conjunction with `fail2ban <http://www.fail2ban.org>`_ to temporarily block IP addresses (usually via iptables). ``fail2ban`` is commonly included with recent Linux distributions. See the fail2ban site for general documentation.

Steps to use collective.tarpit with fail2ban:

1. Install fail2ban and collective.tarpit

2. Check to make sure that failed Plone logins are indeed logged to /var/log/auth.log

3. To the ``filters.d`` directory of the fail2ban configuration, add a plone.conf filter definition for collective.tarpit::

    [INCLUDES]
    before = common.conf
    [Definition]
    _daemon = plone
    failregex = ^%(__prefix_line)sAuthentication failure for .* site .* from <HOST>$
    ignoreregex =

    A sample is included inside the filter.d directory of this package.

4. Create, if necessary, a jail.local file in the directory containing jail.conf. Add to it::

    [plone]
    enabled = true
    port = http,https
    filter = plone
    logpath = /var/log/auth.log
    maxretry = 6

Adjusting ``maxretry`` to meet your needs.
