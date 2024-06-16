"""
init sql alchemy client model
"""
from sqlalchemy.sql import func

from sqlalchemy import Column, BigInteger, String, DateTime, Boolean, Float

from app.bot import models
from app.bot.services.external.alchemy import Base
from app.bot.services.external.alchemy import Session


# pylint: disable=E1102
class Client(Base):
    """
    Client model representing a user in the database.
    """
    __tablename__ = 'telegram_user'

    id = Column(BigInteger, primary_key=True)
    username = Column(String, unique=True)  # Ensure unique usernames
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    lang = Column(String, default="ru", nullable=True)
    is_active = Column(Boolean)
    phone = Column(BigInteger, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    state = Column(String, nullable=True)
    is_state_notified = Column(Boolean)


async def create_or_update_client(
    client: models.Client,
):
    """
    function to create or update a client in the database
    """
    with Session() as session:
        user = session.query(Client).filter_by(
            username=client.username
        ).first()

        if user:
            user.first_name = client.first_name
            user.last_name = client.last_name

        if not user:
            user = Client(
                id=client.chat_id,
                username=client.username,
                first_name=client.first_name,
                last_name=client.last_name,
                is_active=True,
                created_at=func.now(),
                updated_at=func.now(),
                state="on_start",
                is_state_notified=False
            )
            session.add(user)

        session.commit()


async def set_user_lang(
    client: models.Client,
    lang: str
):
    """
    this function helps to set the user language
    """
    with Session() as session:
        user = session.query(Client).filter_by(
            id=client.chat_id
        ).first()

        if user:
            user.lang = lang

        session.commit()


async def get_user_lang(
    client: models.Client
) -> str:
    """
    this function helps to get the user language
    """
    with Session() as session:
        user = session.query(Client).filter_by(
            id=client.chat_id
        ).first()

        if user:
            return user.lang

        return "uz"


async def swich_state(
    chat_id: int,
    state: str
):
    """
    this function helps to set the user language
    """
    with Session() as session:
        user = session.query(Client).filter_by(
            id=chat_id
        ).first()

        if user:
            user.state = state
            user.is_state_notified = False

        session.commit()
