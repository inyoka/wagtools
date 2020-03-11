from django.db import models

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    FieldPanel,
)
from wagtail.snippets.models import register_snippet


class Seo(models.Model):
    ''' Add extra seo fields to pages such as icons. '''
    google_ad_code = models.CharField(max_length=50, null=True, blank=True)
    seo_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Optional social media image 300x300px image < 300kb."
    )

    panels = [
        MultiFieldPanel(
            [
                ImageChooserPanel('seo_image'),
                FieldPanel('google_ad_code'),
            ],
            heading="Additional SEO options ...",
        )

    ]

    class Meta:
        """Abstract Model."""
        abstract = True



@register_snippet
class Google(models.Model):
    site_tag = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Google site code"
        verbose_name_plural = "Google site code"

    panels = [
        FieldPanel('site_tag'),
    ]

    def __str__(self):
        return self.site_tag

@register_snippet
class Facebook(models.Model):
    site_tag = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Facebook site code"
        verbose_name_plural = "Facebook site code"

    panels = [
        FieldPanel('site_tag'),
    ]

    def __str__(self):
        return self.site_tag


@register_snippet
class Links(models.Model):
    text = models.CharField("Visible text (eg. Latest School Bulletin)", max_length=255, null=True, blank=True)  # eg. Decembers Bulletin
    link = models.CharField("Link to resource (eg tel:+62-061-661-6765)", max_length=255, null=True, blank=True)
    hover = models.CharField("Desc on hover (eg. December Bulletin)", max_length=255, null=True, blank=True)  # eg. Latest School Bulletin
    icon = models.CharField("FA Icon (eg. fas fa-newspaper fa-fw fa-2x)", max_length=255, null=True, blank=True)
    css = models.CharField("List CSS Classes (eg. text-primary py-0)", max_length=255, null=True, blank=True)  # eg. text-primary py-0 fa-2x

    class Meta:
        verbose_name = "Social Media link and icon"
        verbose_name_plural = "Social Media links and icons"


    panels = [
        FieldPanel('text'),
        FieldPanel('link'),
        FieldPanel('hover'),
        FieldPanel('icon'),
        FieldPanel('css'),
    ]


    def __str__(self):
        if self.text==None:
            return self.hover
        return self.text
