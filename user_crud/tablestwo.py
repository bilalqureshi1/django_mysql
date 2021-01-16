
from flask_table import Table, Col, LinkCol
"""
below class is used to display spaceship table. It's used in main.py
"""
class Resultb(Table):
    spaceid = Col('spaceid')
    name = Col('name')
    model = Col('model')
    status = Col('status')
    city_name = Col('city_name')
    planet_name = Col('planet_name')

    edit = LinkCol('Edit', 'edit_view_spaceship', url_kwargs=dict(id='spaceid'))
    delete = LinkCol('Delete', 'delete_spaceship_user', url_kwargs=dict(id='spaceid'))