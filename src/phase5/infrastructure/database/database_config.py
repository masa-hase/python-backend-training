"""
データベース設定

【課題12】SQLAlchemyのデータベース設定をTDDで実装してください
"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from .models import Base


class DatabaseConfig:
    """データベース設定クラス"""
    
    def __init__(self, database_url: str):
        self.database_url = database_url
        self.engine = create_async_engine(database_url)
        self.SessionLocal = sessionmaker(
            self.engine, 
            class_=AsyncSession, 
            expire_on_commit=False
        )
    
    async def create_tables(self):
        """テーブル作成"""
        # TODO: TDDで実装してください
        pass
    
    async def drop_tables(self):
        """テーブル削除"""
        # TODO: TDDで実装してください
        pass
    
    async def get_session(self) -> AsyncSession:
        """データベースセッションを取得"""
        # TODO: TDDで実装してください
        pass
    
    async def close(self):
        """接続を閉じる"""
        # TODO: TDDで実装してください
        pass


# デフォルト設定
DATABASE_URL = "sqlite+aiosqlite:///./app.db"
database_config = DatabaseConfig(DATABASE_URL)


async def get_database_session():
    """FastAPI依存性注入用のデータベースセッション取得"""
    # TODO: TDDで実装してください
    pass