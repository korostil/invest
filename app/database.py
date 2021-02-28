import motor.motor_asyncio

from app.settings import Settings

client = motor.motor_asyncio.AsyncIOMotorClient(
    Settings.mongodb_host, Settings.mongodb_port
)

database = client.invest
