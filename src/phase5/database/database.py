"""
データベース設定とモデル定義

【課題1】SQLAlchemyでデータベース設定を実装してください
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from datetime import datetime

DATABASE_URL = "sqlite+aiosqlite:///./app.db"  # 開発用SQLite
# DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"  # 本番用

Base = declarative_base()


class User(Base):
    """ユーザーモデル"""
    __tablename__ = "users"
    
    # TODO: 実装してください
    pass


class LogFile(Base):
    """ログファイルモデル"""
    __tablename__ = "log_files"
    
    # TODO: 実装してください
    pass


class LogEntry(Base):
    """ログエントリモデル"""
    __tablename__ = "log_entries"
    
    # TODO: 実装してください
    pass


# データベースエンジンとセッション
engine = create_async_engine(DATABASE_URL)
SessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_database():
    """データベースセッションを取得"""
    # TODO: 実装してください
    pass