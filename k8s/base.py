from k8s.core.secret import Secret
from k8s.core.config import Config


class Base(object):

    _cf = Config().data()

    def run(self):
        Secret(**self._cf).run()
