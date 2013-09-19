import tornado
import tornado.template
import os
from tornado.options import define

# Make filepaths relative to settings.
path = lambda root, *a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

define("port", default=9090, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")
tornado.options.parse_command_line()

MEDIA_ROOT = path(ROOT, 'media')
TEMPLATE_ROOT = path(ROOT, 'templates')

# Deployment Configuration
settings = {}
settings['debug'] = False
settings['static_path'] = MEDIA_ROOT
settings['cookie_secret'] = 'cookies!'
#settings['xsrf_cookies'] = True
settings['gzip'] = True
settings['template_loader'] = tornado.template.Loader(TEMPLATE_ROOT)
settings['login_url'] = "/login"
settings['facebook_api_key'] = ''
settings['facebook_secret'] = ''
settings['twitter_consumer_key'] = ''
tcs = ''
settings['twitter_consumer_secret'] = tcs
