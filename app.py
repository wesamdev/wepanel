from flask import Flask
import importlib
import routes.login as loginroute
app = Flask(__name__)
app.secret_key = 'daldol'
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
        {
        'url': '/login/callback',
        'module': 'routes.login',
        'function': 'callback'
    },
            {
        'url': '/login/discord',
        'module': 'routes.login',
        'function': 'discord_login'
    },
                {
        'url': '/dash/user/info',
        'module': 'routes.userinfo',
        'function': 'userinfo'
    },
                    {
        'url': '/dash',
        'module': 'routes.dashboard',
        'function': 'dashboard'
    },
                        {
        'url': '/api/logout',
        'module': 'api.logout',
        'function': 'logout'
    },
]
loginroute.init_outh(app)
# Register the routes
register_routes(app, routes)




if __name__ == '__main__':
    app.run(debug=True) # disable this if you want to run on production and run server on wsgi
