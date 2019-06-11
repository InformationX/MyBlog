#!/usr/bin/env python
# encoding: utf-8
from django import template
from django.conf import settings
import markdown
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import random

register = template.Library()


@register.simple_tag
def timeformat(data):
    try:
        return data.strftime(settings.TIME_FORMAT)
        # print(data.strftime(settings.TIME_FORMAT))
        # return "ddd"
    except:
        return ""


@register.filter(is_safe=True)
@stringfilter
def custom_markdown(content):
    return mark_safe(markdown.markdown(content,
                                       extensions=
                                       ['markdown.extensions.fenced_code',
                                        'markdown.extensions.codehilite'],
                                       safe_mode=True, enable_attributes=False))


@register.inclusion_tag('blog/categorytree.html')
def parsecategoryname(article):
    names = article.get_category_tree()

    names.append((settings.SITE_NAME, 'http://127.0.0.1:8000'))
    names = names[::-1]
    print(names)
    return {'names': names}


@register.inclusion_tag('blog/articletaglist.html')
def loadarticletags(article):
    tags = article.tags.all()
    tags_list = []
    for tag in tags:
        url = tag.get_absolute_url()
        count = tag.get_article_count()
        tags_list.append((
            url, count, tag, random.choice(settings.BOOTSTRAP_COLOR_TYPES)
        ))
    return {
        'article_tags_list': tags_list
    }
