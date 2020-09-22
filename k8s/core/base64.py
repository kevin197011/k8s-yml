import base64



class Base64:

    def encode(self, file) -> str:
        with open(f"resources/files/{file}", "rb") as f:
            _context = f.read()
        return base64.b64encode(_context).decode("utf-8") 
