from django import template
from mmo.apps.characters.models import Character

register = template.Library()


@register.inclusion_tag("characters/sidebar.html", takes_context=True)
def sidebar(context):
    return {
         "characters": Character.objects.filter(
            user=context['user']
        )
    }
