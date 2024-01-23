import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.0"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.mydb

collection = database.get_collection("ebay")

def article_helper(article) -> dict:
    return {
        "id": str(article["_id"]),
        "titre": article["titre"],
        "prix": float(article["prix"]),
    }

async def retrieve_articles():
    articles = []
    async for article in collection.find():
        articles.append(article_helper(article))
    return articles

async def add_article(data: dict) -> dict:
    article = await collection.insert_one(data)
    new_article = await collection.find_one({"_id": article.inserted_id})
    return article_helper(new_article)

async def retrieve_article(id: str) -> dict:
    article = await collection.find_one({"_id": ObjectId(id)})
    if article:
        return article_helper(article)

async def update_article(id: str, data: dict):
    if len(data) < 1:
        return False
    article = await collection.find_one({"_id": ObjectId(id)})
    if article:
        updated_article = await collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_article:
            return True
        return False

async def delete_article(id: str):
    article = await collection.find_one({"_id": ObjectId(id)})
    if article:
        await collection.delete_one({"_id": ObjectId(id)})
        return True
    