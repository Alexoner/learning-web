from django.shortcuts import render

from todo.models import *
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect

# Create your views here.


@staff_member_required
def mark_done(request, pk):
    item = Item.objects.get(pk=pk)
    item.done = True
    item.save()
    return HttpResponseRedirect(reverse("admin:todo_item_changelist"))


@staff_member_required
def item_action(request, action, pk):
    """ Mark done,toggl onhold or delete a todo item."""
    if action == "done":
        item = Item.objects.get(pk=pk)
        item.done = True
        item.save()
    elif action == "onhold":
        item = Item.objects.get(pk=pk)
        if item.onhold:
            item.onhold = False
        else:
            item.onhold = True
        item.save()
    elif action == "delete":
        Item.objects.filter(pk=pk).delete()

    return HttpResponseRedirect(reverse("admin:todo_item_changelist"))


@staff_member_required
def onhold_done(request, mode, action, pk):
    """Toggle Done/ onhold on/off"""
    item = Item.objects.get(pk=pk)

    if action == "on":
        if mode == "done":
            item.done = True
        elif mode == "onhold":
            item.onhold = True
    elif action == "off":
        if mode == "done":
            item.done = False
        elif mode == "onhold":
            item.onhold = False

    item.save()
    return HttpResponse('')


def progress(request, pk):
    """Set task progress"""
    p = request.POST
    if "progress" in p:
        item = Item.objects.get(pk=pk)
        item.progress = int(p["progress"])
        item.save()
    return HttpResponse('')
