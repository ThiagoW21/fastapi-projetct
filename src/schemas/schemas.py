from pydantic import BaseModel


class Token(BaseModel):
    token: str

    class Config:
        orm_mode = True


class UserSimple(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int | None = None
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True


class LoginData(BaseModel):
    password: str
    email: str


class LoginSucess(BaseModel):
    user: UserSimple
    access_token: str


class Collaborator(BaseModel):
    id: int | None = None
    full_name: str
    gender: str
    tel: str
    email: str
    office: str
    cep: int
    city: str
    state: str
    public_place: str
    number: int
    complement: str
    district: str
    data_nasc: str
    reference_point: str

    class Config:
        orm_mode = True


class Item(BaseModel):
    id: int | None = None
    code: int
    title: str
    category: str
    url_image: str
    brand: str
    model: str
    description: str
    borrowed_to: str | None = 'Na empresa'
    price: float

    class Config:
        orm_mode = True
