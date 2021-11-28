import motor.motor_asyncio
from umongo.frameworks import MotorAsyncIOInstance

from app.settings import settings

client = motor.motor_asyncio.AsyncIOMotorClient(
    settings.mongodb_host, settings.mongodb_port
)

database = client[settings.mongodb_database]

motor_instance = MotorAsyncIOInstance(database)
