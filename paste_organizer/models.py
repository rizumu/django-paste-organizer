from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
try:
    from tagging.fields import TagField
except:
    TagField = None

class Pastebin(models.Model):
    """
    Online service where your paste is hosted
    """
    pastebin_name = models.CharField(blank=True, max_length=100)
    create_paste_url = models.URLField(blank=True, verify_exists=True)
    paste_url = models.URLField(blank=True, verify_exists=True)

    def __unicode__(self):
        return self.pastebin_name

    class Meta(object):
        verbose_name = _('pastebin')
        verbose_name_plural = _('pastebins')
        ordering=['pastebin_name']

    def create_paste():
        return self.create_paste_url

class Paste(models.Model):
    """
    Plaintext password field could simply be filled in with a reminder of.
    """
    paste_name = models.CharField(_('paste name'), max_length=100)
    pastebin_type = models.ForeignKey(Pastebin)
    creator = models.ForeignKey(User, related_name=_("creator"))
    create_date = models.DateTimeField(_("created"), default=datetime.now)
    paste_id = models.CharField(_('paste id'), max_length=25)
    if TagField:
        tags = TagField()
    plaintext_password = models.CharField(_('plaintext password'), 
        max_length=100, blank =True, null =True, help_text="no encryption")
    active = models.BooleanField(default=True)
    public = models.BooleanField(default=True)

    def __unicode__(self):
        return self.paste_name

    class Meta(object):
        verbose_name = _('paste')
        verbose_name_plural = _('pastes')
        ordering=['create_date']

    def url(self):
        return "%s%s" % (self.pastebin_type.paste_url, self.paste_id)
