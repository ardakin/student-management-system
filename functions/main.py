from firebase_functions import https_fn
from firebase_functions.options import set_global_options
from werkzeug.test import run_wsgi_app
from werkzeug.wrappers import Response
from app import app as flask_app  # app.py içindeki Flask app

set_global_options(region="us-central1", max_instances=10)

@https_fn.on_request()
def serving(req: https_fn.Request) -> https_fn.Response:
    """
    Firebase Hosting'ten gelen tüm HTTP istekleri buraya düşecek.
    Flask WSGI pipeline'ını eksiksiz çalıştırıp Set-Cookie ve yanıtı döndürüyoruz.
    """
    app_iter, status, headers = run_wsgi_app(flask_app, req.environ)
    return Response(app_iter, status=status, headers=headers)

