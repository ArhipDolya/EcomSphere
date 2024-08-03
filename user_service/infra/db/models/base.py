from datetime import datetime
from pydantic import BaseModel

from sqlalchemy import MetaData, func
from sqlalchemy.orm import declarative_base, mapped_column


metadata = MetaData()

Base = declarative_base(metadata=metadata)


class TimedBaseModel(BaseModel):
    """An abstract base model that adds created_at and updated_at timestamp fields to the model"""

    __abstract__ = True

    created_at: datetime = mapped_column(default=func.now(), nullable=False)
    updated_at: datetime = mapped_column(
        default=func.now(), onupdate=func.now(), nullable=False
    )
