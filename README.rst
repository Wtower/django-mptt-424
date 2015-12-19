===============
django-mptt-424
===============

Minified verifiable example for `Django mptt issue #424`_

.. _Django mptt issue #424: https://github.com/django-mptt/django-mptt/issues/424

How to reproduce
----------------

1. Download project

2. Create a virtualenv and install requirements::

       $ mkvirtualenv mptt_424 --python=`which python3` --no-site-packages
       $ source ~/.virtualenvs/mptt_424/bin/activate  # or whatever path
       $ pip install -r requirements.txt

   The requirements to reproduce is:

   - Django 1.9.0
   - Latest mptt master (at least as of Dec 19 2015)

3. A default ``db.sqlite3`` is included, otherwise specify a different db source and::

       $ ./manage.py migrate
       $ ./manage.py loaddata mptt

4. Run server

       $ ./manage.py runserver

   and navigate to ``http://127.0.0.1:8000/en/about/``.

Important files
---------------

Most code is isolated from `NineCMS`_ project.

.. _NineCMS: https://github.com/Wtower/django-ninecms

1. ``mptt_424/settings.py``

   The following settings are different from defaults (can also inspect them with diff from initial commit):

   1. ``INSTALLED_APPS`` include ``mptt`` and the auxiliary application ``mptt_424_app``.
   2. ``TEMPLATES`` include the folder ``templates`` and specify debug true.
   3. ``LANGUAGE_CODE`` is ``en``.

2. ``mptt_424_app/models.py``

   Includes the ``MenuItem`` mptt model and an unimportant helper function.

3. ``mptt_424_app/fixtures/mptt.json``

   Includes initial data for testing. They are included in bundled ``db.sqlite3`` file.

4. ``mptt_424/urls.py``, ``mptt_424_app/urls.py``

   Default urls files that call our view.

5. ``mptt_424_app/views.py``

   Defines one view that renders the following template. What is noteable in this view is that context is::

       menu = MenuItem.objects.get(pk=1).get_descendants()

6. ``templates/mpt_424_app/block_menu_header.html``

   Our default template that renders a menu based on our model. The template calls a custom template tag
   that returns the active trail (btw any other recommended method is welcome, but still the bug remains).

7. ``mptt_424_app/templatetags/mptt_424_extras.py``

   Custom template tag that returns the active trail::

       return menu.filter(path=get_clean_url(url)).get_ancestors(include_self=True)

