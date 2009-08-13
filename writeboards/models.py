from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from tagging.models import Tag
from tagging.fields import TagField

class Writeboard(models.model):
    """
    Plaintext password field could simply be filled in with a reminder of.
    """
    writeboard_name = models.CharField(_('writeboard name'), max_length=100)
    slug = models.SlugField(_('slug'), unique=True)
    creator = models.ForeignKey(_('creator'), User, related_name=_("creator"))
    create_date = models.DateTimeField(_("created"), default=datetime.now)
    writeboard_id = models.IntegerField(_('writeboard id'),)
    tags = TagField()
    public = models.BooleanField(default=True)
    plaintext_password = models.CharField(_('plaintext password'), 
        max_length=100, blank =True, null =True, help_text="no encryption")
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.writeboard_name

    class Meta(object):
        verbose_name = _('writeboard')
        verbose_name_plural = _('writeboards')
        ordering=['modified']

    def create_a_writeboard():
        return ('http://writeboard.com/')

    @models.permalink
    def get_absolute_url(self):
        return ('writeboard_detail', None, {'slug': self.slug})
