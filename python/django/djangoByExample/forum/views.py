from django.shortcuts import render, render_to_response
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


def post(request, ptype, pk):
    """Display a post form."""
    action = reverse("forum.views.%s" % ptype, args=[pk])
    if ptype == "new_thread":
        title = "Start New Topic"
        subject = ''
    elif ptype == "replay":
        title = "Reply"
        subject = "Re:" + Thread.objects.get(pk=pk).title

    return render_to_response("forum/post.html",
                              add_scrf(request, subject=subject,
                                       action=action, title=title))


def new_thread(request, pk):
    """Start a new thread"""
    p = request.POST
    if p["subject"] and p["body"]:
        forum = Forum.objects.get(pk=pk)
        thread = Thread.objects.create(forum=forum, title=p["subject"],
                                       creator=request.user)
        Post.objects.create(thread=thread, title=p["subject"],
                            body=p["body"], creator=request.user)
    return HttpResponseRedirect(reverse("forum.views.forum", args=[pk]))


def reply(request, pk):
    """Reply to a thread."""
    p = request.POST
    if p["body"]:
        thread = Thread.objects.get(pk=pk)
        post = Post.objects.create(thread=thread, title=p["subject"],
                                   body=p["body"],
                                   creator=request.user)

    return HttpResponseRedirect(reverse("forum.views.thread", args=[pk]) +
                                "?page=last")
