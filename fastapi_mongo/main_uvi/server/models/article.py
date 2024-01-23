from pydantic import BaseModel, Field

class ArticleSchema(BaseModel):
    titre: str = Field(...)
    prix_article: float = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "titre": "test_titre",
                "prix": 222,
            }
        }


class UpdateArticleModel(BaseModel):
    titre: str = Field(...)
    prix_article: float = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "titre": "update_test_titre",
                "prix_article": 222,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }



def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}