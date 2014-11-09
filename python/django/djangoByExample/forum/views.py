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
