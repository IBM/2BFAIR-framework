from pydantic import BaseModel


class LicenseInformation(BaseModel):
    raw_value: str
