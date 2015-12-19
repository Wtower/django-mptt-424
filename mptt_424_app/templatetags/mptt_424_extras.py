
from django import template

register = template.Library()


def get_clean_url(url):
    """ Get a url without the language part, if i18n urls are defined
    :param url: a string with the url to clean
    :return: a string with the cleaned url
    """
    url = url.strip('/')
    url = '/' if not url else url
    return '/'.join(url.split('/')[1:])


@register.filter
def active_trail(menu, url):
    """ Get the active menu item based on url provided, and all of its ancestors
    To be used to check each individual node's path if in this list so to obtain the active trail
    Also remove language part from url if i18n urls are enabled
    :param menu: the parent menu
    :param url: the current url to check against for the active path (should be request.path)
    :return: a recordset of all active menu ancestors
    """
    return menu.filter(path=get_clean_url(url)).get_ancestors(include_self=True)


@register.filter
def flatten(records, fld):
    """ Flatten a recordset to list of a particular field
    :param records: the recordset to flatten
    :param fld: the field from the records to include in list
    :return: a list
    """
    return [path for fields in records.values_list(fld) for path in fields]


@register.filter
def check_path_active(node_path, request_path):
    """ Check that the two paths are equal, ignoring leading or trailing slashes
    Helper function for improving readability
    Mainly used in menu templates
    :param node_path: the menu item path
    :param request_path: the request path
    :return: boolean
    """
    url = get_clean_url(request_path)
    return node_path == url or node_path == url.strip('/')
