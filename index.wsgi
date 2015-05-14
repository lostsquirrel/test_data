import application
import sae

app = application.Application()
application = sae.create_wsgi_app(app)
