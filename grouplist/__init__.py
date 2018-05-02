# -*- coding: utf-8 -*-
"""
    grouplist
    ~~~~~~~~~

    A grouplist Plugin for FlaskBB.

    :copyright: (c) 2018 by Михаил Лебедев.
    :license: BSD License, see LICENSE for more details.
"""
from flask import render_template_string


__version__ = "0.0.1"


def flaskbb_tpl_post_author_info_after(user, post):
    return render_template_string('''
    <div style="text-shadow: none;">
        {% for group in user.secondary_groups %}
            <span class="label label-default">{{ group.name }}</span>
        {% endfor %}
    </div>
    ''', user=user)


SETTINGS = {}
