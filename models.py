# pylint: disable=E1101

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable, Site
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel
)
from wagtail.images.edit_handlers import (
    ImageChooserPanel
)

from wagtail.core.fields import (
    RichTextField, 
    StreamField
)
from wagtail.core.blocks import (
    URLBlock, 
    TextBlock, 
    StructBlock, 
    StreamBlock, 
    CharBlock, 
    RichTextBlock, 
    BooleanBlock
)
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)
from wagtail.admin.edit_handlers import (
    FieldPanel, 
    StreamFieldPanel
)

from wagtail.search import index

from wagtools.snippet import Seo, Google, Facebook, SocialLinks, EditableFooter
from wagtools.blocks import CommonStreamBlock


class DefaultHomePage(Page, Seo):
    my_stream = StreamField(CommonStreamBlock(required=False), null=True, blank=True)

    def get_context(self, request):
        context = super(DefaultHomePage, self).get_context(request)
        context['menuitems'] = Site.find_for_request(request).root_page.get_descendants(
            inclusive=True).live().in_menu()
        return context

    search_fields = Page.search_fields + [
        index.SearchField('my_stream'),
    ]

    content_panels = Page.content_panels + [
        StreamFieldPanel('my_stream', "Main content..."),
    ]
    promote_panels = Page.promote_panels + Seo.panels

    template = 'home/home_page.html'


class SectionIndexPage(Page, Seo):
    alt_template = models.IntegerField(
        verbose_name="Index-page style? 1) List 2) Card 3) Card & Image",
        default=1,
        validators=[MaxValueValidator(3), MinValueValidator(1)]
        )

    my_stream = StreamField(CommonStreamBlock(), null=True, blank=True)

    def get_template(self, request):
        if self.alt_template == 1:
            return 'sections/index_page_list.html'
        elif self.alt_template == 2:
            return 'sections/index_page_cards.html'
        elif self.alt_template == 3:
            return 'sections/index_page_image.html'
        else :
            return 'sections/list_index_page.html'

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        if self.alt_template:
            blogpages = self.get_children().live()
            context['blogpages'] = blogpages
        else : 
            blogpages = self.get_children().live().order_by('-first_published_at')
            context['blogpages'] = blogpages
        context['menuitems'] = Site.find_for_request(request).root_page.get_descendants(
            inclusive=True).live().in_menu()
        return context

    search_fields = Page.search_fields + [
        index.SearchField('my_stream'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('alt_template'),
        StreamFieldPanel('my_stream')
    ]
    promote_panels = Page.promote_panels + Seo.panels


class SectionPage(Page, Seo):
    body = RichTextField(blank=True)
    my_stream = StreamField(CommonStreamBlock(), null=True, blank=True,)

    parent_page_types = ['wagtools.SectionIndexPage']

    def get_template(self, request):
        return 'sections/section_page.html'

    def get_context(self, request):
        context = super(SectionPage, self).get_context(request)
        context['menuitems'] = Site.find_for_request(request).root_page.get_descendants(
            inclusive=True).live().in_menu()
        return context
    
    def prev_section(self):
        if self.get_prev_sibling():
            return self.get_prev_sibling()
        else:
            return self.get_siblings().last()

    def next_section(self):
        if self.get_next_sibling():
            return self.get_next_sibling()
        else:
            return self.get_siblings().first()


    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.SearchField('my_stream'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        StreamFieldPanel('my_stream'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]
    promote_panels = Page.promote_panels + Seo.panels

class SectionGalleryImage(Orderable):
    page = ParentalKey(SectionPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+',
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage', 
        on_delete=models.CASCADE,
        related_name='form_fields',
    )
    
class ContactPage(AbstractEmailForm, Seo):
    my_stream = StreamField(CommonStreamBlock(), null=True, blank=True,)
    thank_you = StreamField(CommonStreamBlock(), null=True, blank=True,)
    css_label = 'Add CSS (FontAwesome and Bootstrap classes) '

    button_css = models.CharField(max_length=300, 
                    default='btn-success', 
                    null=True, blank=True, 
                    verbose_name= 'Button CSS',
                    help_text= 'Classes from FontAwesome and Bootstrap can be used')
    button_text = models.CharField(max_length=300, 
                    default='Submit', 
                    null=True, blank=True,
                    help_text= 'FontAwesome icons can be used')
 
    template = 'contact/contact_page.html'
    def get_context(self, request):
        context = super(ContactPage, self).get_context(request)
        context['menuitems'] = Site.find_for_request(request).root_page.get_descendants(inclusive=True).live().in_menu()
        return context

    content_panels = AbstractEmailForm.content_panels + [
        StreamFieldPanel('my_stream'),
        InlinePanel('form_fields', label='Form Fields'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('button_text', classname='col4'),
                FieldPanel('button_css', classname='col8'),
            ]),
        ], heading='Button Settings'),
        StreamFieldPanel('thank_you'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname='col6'),
                FieldPanel('to_address', classname='col6'),
            ]),
            FieldPanel('subject'),
        ], heading='Email Settings'),
    ]
    
    promote_panels = AbstractEmailForm.promote_panels + Seo.panels

class OrphanContactPage(ContactPage):
        template = 'contact/orphan_contact_page.html'
