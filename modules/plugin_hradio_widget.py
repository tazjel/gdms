# -*- coding: utf-8 -*-
# This plugins is licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php
# Authors: Kenji Hosoda <hosoda@s-cubism.jp>
# hcheck widget added by DMcC - seems to be an additional disabled row at end of it for some reason
from gluon import *


def hradio_widget(field, value, **attributes):
    rows = SQLFORM.widgets.radio.widget(field, value).elements('tr')
    inner = []
    for row in rows:
        button, label = row.elements('td')[0]
        button.attributes['_style'] = 'cursor:pointer;'
        label.attributes.update(_for=button.attributes['_id'],
                                _style='cursor:pointer;')
        inner.append(SPAN(button, ' ', label, _style='padding-right:10px;'))
    return DIV(*inner, **attributes)


def hcheck_widget(field, value, **attributes):
    rows = SQLFORM.widgets.checkboxes.widget(field, value).elements('tr')
    inner = []
    for row in rows[:-1]:
        print row.elements('td')[0]
        button, label = row.elements('td')[0]
        button.attributes['_style'] = 'cursor:pointer;'
        label.attributes.update(_for=button.attributes['_id'],
                                _style='cursor:pointer;')
        inner.append(SPAN(button, ' ', label, _style='padding-right:10px;'))
    return DIV(*inner, **attributes)