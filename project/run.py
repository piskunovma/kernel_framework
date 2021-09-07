from framework.main import Framework
from project.routes import routes
from project.front_controllers import fronts
from wsgiref.simple_server import make_server

application = Framework(routes, fronts)

with make_server('', 8000, application) as httpd:
    print("Запуск на порту 8000...")
    httpd.serve_forever()
