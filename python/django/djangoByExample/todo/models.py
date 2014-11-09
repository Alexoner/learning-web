from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from djangoByExample.settings import STATIC_URL

# Create your models here.


class DateTime(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.datetime.strftime("%b %d,%Y,%I:%M %p"))


class Item(models.Model):
    name = models.CharField(max_length=60)
    created = models.ForeignKey(DateTime)
    priority = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    done = models.BooleanField(default=False)
    onhold = models.BooleanField(default=False)
    user = models.ForeignKey(User, blank=True, null=True)
    progress = models.IntegerField(default=0)

    # def progress_(self):
        # return "<div style='width:100px;border:1px solid #ccc;'>" +\
            # "<div style='height:4px;width:%dpx;background:#555;'>\
            #</div></div>" % (self.progress)

    def progress_(self):
        return """
            <div id="progress_count_%s" class="progress_count">
            <div id="progress_btns_%s" class="progress_btns">
                <ul>
                    <li>10</li>
                    <li>20</li>
                    <li>30</li>
                    <li>40</li>
                    <li>50</li>
                    <li>60</li>
                    <li>70</li>
                    <li>80</li>
                    <li>90</li>
                    <li>100</li>
                </ul>
            </div>
            <div id="progress_on_%s" class="progress_on">&nbsp;</div>
            <div id="progress_%s" style="visibility:hidden"></div>
            </div>
            """ % (self.pk, self.pk, self.pk, self.pk)

    progress_.allow_tags = True
    progress_.admin_order_field = "progress"

    def onhold_(self):
        if self.onhold:
            btn = "<div id='onhold_%s'><img class='btn' src='%simg/admin/icon-on.gif' /></div>"
        else:
            btn = "<div id='onhold_%s'><img class='btn' src='%simg/admin/icon-off.gif' /></div>"
        return btn % (self.pk, STATIC_URL)
    onhold_.allow_tags = True
    onhold_.admin_order_field = "onhold"
    onhold_.short_description = "onhold"

    def done_(self):
        if self.done:
            btn = "<div id='done_%s'><img class='btn' \
                src='%simg/admin/icon-on.gif' /></div>"
        else:
            btn = "<div id='done_%s'><img class='btn' \
                src='%simg/admin/icon-off.gif' /></div>"
        return btn % (self.pk, STATIC_URL)
    done_.allow_tags = True
    done_.admin_order_field = "done"

    # def delete(self):
        # url = reverse("todo.views.item_action", args=["delete", self.pk])
        # return "<a href='%s'>Delete</a>" % url
    # delete.allow_tags = True

    def mark_done(self):
        return "<a href='%s'>Done</a>" % reverse("todo.views.mark_done",
                                                 args=[self.pk])
    mark_done.allow_tags = True
    mark_done.admin_order_field = 'mark_done'
    mark_done.short_description = 'mark as done'
