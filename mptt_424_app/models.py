
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


def get_full_path(path, language, bookmark=''):
    """ Utility function to build a valid path based on an initial
    :param path: the initial path
    :param language: language component
    :param bookmark: bookmark, if any
    :return: a valid path string
    """
    if not path.startswith('/'):
        path = '/' + path
    if not path.endswith('/'):
        path += '/'
    path += bookmark
    if language:
        path = '/' + language + path
    return path


class MenuItem(MPTTModel):
    """ Menu Item Model: menu tree item in a single tree, paths can be empty for parents """
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    weight = models.IntegerField(default=0, db_index=True)
    language = models.CharField(max_length=2, blank=True)
    path = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        """ Get model name
        :return: model name
        """
        return str(self.title)

    def full_path(self):
        """ Get the full path including language (if any) and path
        @see 9cms_menu_full_path.ods
        :return: full path string
        """
        path = self.path
        if path.startswith('http:') or path.startswith('https:'):
            return path
        if path.startswith('#'):
            return path
        bookmark = ''
        bookmark_pos = path.find('#')
        if bookmark_pos > 0:
            bookmark = path[bookmark_pos:]
            path = path[:bookmark_pos]
        return get_full_path(path, self.language, bookmark)

    class MPTTMeta:
        """ Set order when inserting items for mptt """
        order_insertion_by = ['weight']
