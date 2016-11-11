from pyramid.view import (
    view_config,
    view_defaults
    )


# Setting default renderer for views
@view_defaults(renderer='home.pt')
class TutorialViews:

    def __init__(self, request):
        self.request = request    

    @property
    def counter(self):
        session = self.request.session
        if 'counter' in session:
            session['counter'] += 1
        else:
            session['counter'] = 1
        return session['counter']    

    # First view, available at http://localhost:6543/
    @view_config(route_name='home')
    def home(self):
        return {'name': 'Home View'}

    # /howdy
    @view_config(route_name='hello')
    def hello(self):
        return {'name': 'Hello View'}
