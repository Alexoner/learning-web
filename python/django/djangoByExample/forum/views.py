from django.shortcuts import render
from django.core.urlresolvers import reverse
from djangoByExample.settings import STATIC_URL

from forum.models import *


# Create your views here.
def main(request):
    """Main listing"""
    forums = Forum.objects.all()
    return render_to_response("forum/list.html",
                              dict(forums=forums, user=request.user))


def add_scrf(request, ** kwargs):
    d = dict(user=request.user, **kwargs)
    d.update(csrf(request))
    return d


def mk_paginator(request, items, num_items):
    """Create and reurn a paginator"""
    paginator = Paginator(items, num_items)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        items = paginator.page(page)
    except (InvalidPage, EmptyPage):
        items = paginator.page(pagintor.num_pages)

    return items


def forum(request, pk):
    """Listing of threads in a forum."""
    threads = Thread.objects.filter(forum=pk).order_by("-created")
    threads = mk_paginator(request, threads, 20)
    return render_to_response("forum/forum.html",
                              add_scrf(request, threads=threads, pk=pk))


def thread(request, pk):
    """Listing of posts in a thread."""
    posts = Post.objects.filter(thead=pk).order_by("created")
    posts = mk_paginator(request, posts, 15)
    title = Thread.objects.get(pk=pk).title

    return render_to_response("forum/thread.html",
                              add_scrf(request, posts=posts, pk=pk,
                                       title=title, media_url=""))
