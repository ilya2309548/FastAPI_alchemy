"""
crear
read
update
delete
"""

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product


async def  get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).order_by(Product.id)
    result:  Result = await session.execute(stmt)
        products = result.scalars().all()
    return  list(products)