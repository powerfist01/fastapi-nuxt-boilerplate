from sqlalchemy.ext.asyncio import AsyncSession
from database.setup import AsyncSessionLocal

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session  # Auto-closes session after use
