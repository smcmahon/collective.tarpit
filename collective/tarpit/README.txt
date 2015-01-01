Tests for collective.tarpit

test setup
----------

    >>> from Testing.ZopeTestCase import user_password
    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()

Plugin setup
------------

    >>> acl_users_url = "%s/acl_users" % self.portal.absolute_url()
    >>> browser.addHeader('Authorization', 'Basic %s:%s' % ('portal_owner', user_password))
    >>> browser.open("%s/manage_main" % acl_users_url)
    >>> browser.url
    'http://nohost/plone/acl_users/manage_main'
    >>> form = browser.getForm(index=0)
    >>> select = form.getControl(name=':action')

collective.tarpit should be in the list of installable plugins:

    >>> 'Tarpit Helper' in select.displayOptions
    True

and we can select it:

    >>> select.getControl('Tarpit Helper').click()
    >>> select.displayValue
    ['Tarpit Helper']
    >>> select.value
    ['manage_addProduct/collective.tarpit/manage_add_tarpit_helper_form']

we add 'Tarpit Helper' to acl_users:

    >>> from collective.tarpit.plugin import TarpitHelper
    >>> myhelper = TarpitHelper('myplugin', 'Tarpit Helper')
    >>> self.portal.acl_users['myplugin'] = myhelper

and so on. Continue your tests here

    >>> 'ALL OK'
    'ALL OK'

