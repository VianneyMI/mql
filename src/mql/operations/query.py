from mql.base import BaseModel


class Find(BaseModel):

    query: dict
    projection: dict | None = None
    options: dict | None = None


class FindOne(Find):
    pass
