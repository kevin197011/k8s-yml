
import yaml
from .base64 import Base64


class Config(Base64):


    def _read(self) -> dict:
        _file = open("config/config.yml", "r")
        _context = _file.read()
        _file.close()
        return yaml.unsafe_load(_context)

    def data(self) -> dict:
        data = self._read()
        secret_data = []
        for item in data['secrets']:
            item_data = {}
            for file in item['data']:
                item_data[file] = Base64().encode(file)
            secret_data.append({'name': item['name'], 'data': item_data})
        data['secrets'] = secret_data
        return data
