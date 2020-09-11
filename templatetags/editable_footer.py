from django import template
from wagtools.snippet import EditableFooter

register = template.Library()

# Social snippets
@register.inclusion_tag('tags/editable_footer.html', takes_context=True)
def editable_footer_tag(context):
    return {
        'footer_elements': EditableFooter.objects.all(),
        'request': context['request'],
    }