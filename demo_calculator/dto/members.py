from pydantic import BaseModel, validator

class Members (BaseModel):
    members: list

@validator('members')
def members_cannot_be_empty(cls, v):
    if len(v) == 0:
        raise ValueError('members cannot be empty')

    for member in v:
        if not isinstance(member, str):
            raise ValueError('members must be a list of strings')
    return v