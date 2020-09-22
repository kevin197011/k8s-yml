from jinja2 import Template



class Secret(object):

    def __init__(self, **kwargs):
        self.data = kwargs['secrets']

    def _read(self) -> str:
        _source = open("templates/secret.yml.j2", "r")
        _context = _source.read()
        _source.close()
        return _context

    def _secret(self, files, name):
        t = Template(self._read()).render(files=files, name=name)
        with open(f"resources/yml/{name}-secret.yml", "w") as f:
            f.write(t)
        print(f"{name}-secret.yml generate sucess...")

    def run(self):
        for i in self.data:
            self._secret(i['data'], i['name'])

        