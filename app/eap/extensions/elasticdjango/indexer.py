from .utils import load_documents


def sync_index(app_name=None, document=None):
    for document in load_documents(app_name, document):
        if hasattr(document, 'sync_index'):
            document.sync_index()


def delete_index(app_name=None, document=None):
    for document in load_documents(app_name, document):
        if hasattr(document, 'delete_index'):
            document.delete_index()
