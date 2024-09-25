from django import template

register = template.Library()


@register.filter
def join_tags(task):
    string = " ".join([tag.name for tag in task.tags.prefetch_related("tasks")])
    return string

