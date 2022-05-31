from typing import Dict

from app.model.form import Form


class DB:
    def __init__(self):
        self.dict: Dict = {}

    async def select(self, name):
        if name is None:
            return [item for item in self.dict.items()]
        result = self.dict.get('name')
        return

    async def put(self, form_data: Form):
        self.dict[form_data.name] = form_data


db = DB()
