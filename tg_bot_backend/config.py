from tortoise import Tortoise

TELEGRAM_BOT_TOKEN = ""


async def init_db():
    await Tortoise.init(
        db_url="postgres:",
        modules={"models": ["models"]}
    )
    await Tortoise.generate_schemas()