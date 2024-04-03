from flask import Flask
import importlib

app = Flask(__name__)

def register_routes(app, routes):
    for route in routes:
        try:
            module = importlib.import_module(route['module'])
            if hasattr(module, route['function']):
                view_func = getattr(module, route['function'])
                app.add_url_rule(route['url'], view_func=view_func)
        except ModuleNotFoundError:
            print(f"Module not found: {route['module']}")

# Define the routes as a list of dictionaries
routes = [
    {
        'url': '/',
        'module': 'routes.home',
        'function': 'home'
    },
        {
        'url': '/login',
        'module': 'routes.login',
        'function': 'login'
    },
]

# Register the routes
register_routes(app, routes)

if __name__ == '__main__':
    app.run()
