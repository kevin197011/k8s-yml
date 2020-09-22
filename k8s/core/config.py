import yaml
from .base64 import Base64


class Config(Base64):
    def _read(self) -> dict:
        _file = open("config/config.yml", "r")
        _context = _file.read()
        _file.close()
        return yaml.unsafe_load(_context)

    def data(self) -> dict:
        _data = self._read()
        _secret_data = []
        for item in _data['secrets']:
            item_data = {}
            for file in item['data']:
                item_data[file] = Base64().encode(file)
            _secret_data.append({
                'name': item['name'],
                'namespace': item['namespace'],
                'data': item_data
            })
        _data['secrets'] = _secret_data
        return _data
