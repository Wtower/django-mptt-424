from django.shortcuts import render
from django.views.generic import View
from mptt_424_app.models import MenuItem


class MpttView(View):
    # noinspection PyUnusedLocal,PyUnresolvedReferences
    def get(self, request, **kwargs):
        # MenuItem.objects.rebuild()
        menu = MenuItem.objects.get(pk=1).get_descendants()
        return render(request, 'mptt_424_app/block_menu_header.html', {'menu': menu})
