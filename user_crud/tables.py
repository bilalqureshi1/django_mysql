# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 19:58:36 2021

@author: bqure
"""


from flask_table import Table, Col, LinkCol
"""
below class is used to display location table. It's used in main.py
"""
class Results(Table):
    ID = Col('ID')
    city_name = Col('city_name')
    planet_name = Col('planet_name')
    capacity = Col('capacity')
    edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(id='ID'))
    delete = LinkCol('Delete', 'delete_user', url_kwargs=dict(id='ID'))