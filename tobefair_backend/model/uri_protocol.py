from pydantic import BaseModel


class URIProtocol(BaseModel):
    name: str
    id: str

    def __eq__(self, value: object) -> bool:
        if isinstance(value, URIProtocol):
            return value.id == self.id and value.name == self.name
        elif isinstance(value, str):
            return value == self.id or value == self.name
        return False
