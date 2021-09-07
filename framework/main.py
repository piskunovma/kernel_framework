from project.routes import routes
from project.front_controllers import fronts
from project.views import NotFound404


class Framework:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        print('work')
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        if path in self.routes:
            view = self.routes[path]
        else:
            view = NotFound404()
        request = {}
        for front in self.fronts:
            front(request)
        print(view(request))
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]


# application = Framework(routes, fronts)

# if __name__ == '__main__':
#     print(routes)
