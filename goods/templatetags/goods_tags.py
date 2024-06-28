from django import template


from goods.models import categories

register = template.Library()

@register.simple_tag()
def teg_categories():
    return categories.objects.all()