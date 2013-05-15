# -*- coding: utf-8 -*-
import cPickle as pickle
from uuid import uuid4


class MCSessionStore:

    def __init__(self, mc_connection, **options):
        self.options = {
            'key_prefix': 'session',
            'expire': 30 * 24 * 60 * 60,
            }
        self.options.update(options)
        self.memcache = mc_connection

    def prefixed(self, sid):
        return '%s:%s' % (self.options['key_prefix'], sid)

    def generate_sid(self, ):
        return uuid4().get_hex()

    def get_session(self, sid):
        data = self.memcache.get(self.prefixed(sid))
        session = pickle.loads(data) if data else dict()
        return session

    def set_session(self, sid, session_data):
        expiry = self.options['expire']
        self.memcache.set(self.prefixed(sid), pickle.dumps(session_data), time=expiry)

    def delete_session(self, sid):
        self.memcache.delete(self.prefixed(sid))


class Session:

    def __init__(self, session_store, sessionid=None):
        self._store = session_store
        self._sessionid = sessionid if sessionid else self._store.generate_sid()
        self._sessiondata = self._store.get_session(self._sessionid)
        self.dirty = False

    def clear(self):
        self._store.delete_session(self._sessionid)

    @property
    def sessionid(self):
        return self._sessionid

    def __getitem__(self, key):
        return self._sessiondata[key]

    def __setitem__(self, key, value):
        self._sessiondata[key] = value
        self._dirty()

    def __delitem__(self, key):
        del self._sessiondata[key]
        self._dirty()

    def __len__(self):
        return len(self._sessiondata)

    def __contains__(self, key):
        return key in self._sessiondata

    def __iter__(self):
        for key in self._sessiondata:
            yield key

    def __repr__(self):
        return self._sessiondata.__repr__()

    def _dirty(self):
        self.dirty = True

    def _save(self):
        self._store.set_session(self._sessionid, self._sessiondata)
        self.dirty = False

    def __del__(self):
        if self.dirty:
            self._save()
