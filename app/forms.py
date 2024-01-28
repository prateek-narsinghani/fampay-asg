from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField

class SearchForm(FlaskForm):
    search_by = SelectField('Search By', choices=[('title', 'Title'), ('channel', 'Channel')])
    search_query = StringField('Search Query')
    order_by = SelectField('Order By', choices=[('published_at', 'Published At')])
    sort = SelectField('Sort', choices=[('desc', 'Descending'), ('asc', 'Ascending')], default='desc')
    submit = SubmitField('Search')