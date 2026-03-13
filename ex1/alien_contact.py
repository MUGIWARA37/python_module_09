from pydantic import model_validator, BaseModel
import enum


class ContactType(enum):
    pass


class AlienContact(BaseModel)