from firebase_functions import https_fn
from firebase_functions.options import set_global_options
from app import app as flask_app  # app.py içindeki Flask app

set_global_options(region="us-central1", max_instances=10)

@https_fn.on_request()
def serving(req: https_fn.Request) -> https_fn.Response:
    """
    Firebase Hosting'ten gelen tüm HTTP istekleri buraya düşecek.
    Biz de isteği Flask app'ine forward edip cevabı geri döndürüyoruz.
    """
    with flask_app.request_context(req.environ):
        return flask_app.full_dispatch_request()
