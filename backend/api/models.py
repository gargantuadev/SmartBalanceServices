from sqlalchemy import Column, String, Date, Numeric, ForeignKey, MetaData
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()
metadata = MetaData()


class User(Base):
    __tablename__ = 'users'
    email = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)  # hashed!


class Wallet(Base):
    __tablename__ = 'wallets'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    created_by = Column(String, ForeignKey('users.email', ondelete='SET NULL'), nullable=False)


class Category(Base):
    __tablename__ = 'categories'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    icon = Column(String, nullable=False)
    color = Column(String, nullable=False)
    user_email = Column(String, ForeignKey('users.email', ondelete='CASCADE'), nullable=False)


class WalletUser(Base):
    __tablename__ = 'wallet_users'
    wallet_id = Column(UUID(as_uuid=True), ForeignKey('wallets.id', ondelete='CASCADE'), primary_key=True)
    user_email = Column(String, ForeignKey('users.email', ondelete='CASCADE'), primary_key=True)


class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    wallet_id = Column(UUID(as_uuid=True), ForeignKey('wallets.id', ondelete='CASCADE'), nullable=False)
    category_id = Column(UUID(as_uuid=True), ForeignKey('categories.id', ondelete='SET NULL'))
    description = Column(String)
    expense_date = Column(Date, nullable=False)
    amount = Column(Numeric, nullable=False)


class WalletCategory(Base):
    __tablename__ = 'wallet_categories'
    wallet_id = Column(UUID(as_uuid=True), ForeignKey('wallets.id', ondelete='CASCADE'), primary_key=True)
    category_id = Column(UUID(as_uuid=True), ForeignKey('categories.id', ondelete='CASCADE'), primary_key=True)
