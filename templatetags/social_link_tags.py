from django import template
from wagtools.snippet import SocialLinks

register = template.Library()

# Social snippets
@register.inclusion_tag('tags/social_links.html', takes_context=True)
def social_links(context):
    return {
        'socials': SocialLinks.objects.all(),
        'request': context['request'],
    }