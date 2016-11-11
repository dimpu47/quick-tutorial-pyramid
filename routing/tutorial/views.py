from pyramid.view import (
    view_config,
    view_defaults
    )


# Setting default renderer for views
@view_defaults(renderer='home.pt')
class TutorialViews:

    def __init__(self, request):
        self.request = request    

    # First view, available at http://localhost:6543/
    @view_config(route_name='home')
    def home(self):
        first=self.request.matchdict['first']
        last=self.request.matchdict['last']
        return {
            'name': 'Home View',
            'first':first,
            'last':last,
        }

