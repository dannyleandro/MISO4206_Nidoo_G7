from __future__ import unicode_literals
from django.conf import settings
import socket


def test_connection_to_db(database_name):
    try:
        db_definition = getattr(settings, 'DATABASES')[database_name]
        s = socket.create_connection((db_definition['HOST'], db_definition['PORT']), 5)
        s.close()
        return True
    except Exception as e:
        print '%s (%s)' % (e.message, type(e))
        return False


class PrimaryReplicaRouter:

    def __init__(self):
        pass

    def db_for_read(self, model, **hints):
        if test_connection_to_db('default'):
            print 'Using Default database'
            return 'default'
        else:
            print 'Using replica database'
            return 'read_replica'

    def db_for_write(self, model, **hints):
        """
        Writes always go to default.
        """
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
