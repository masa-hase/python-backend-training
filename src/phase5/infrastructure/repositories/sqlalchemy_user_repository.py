"""
SQLAlchemy ユーザーリポジトリ実装

【課題13】リポジトリパターンの実装をTDDで実装してください

リポジトリ実装の特徴:
- インフラ層のコンポーネント
- ドメインリポジトリインターフェースの実装
- ドメインエンティティとデータモデルの変換
"""

from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from ...domain.entities.user import User
from ...domain.value_objects.email import Email
from ...domain.value_objects.user_name import UserName
from ...domain.repositories.i_user_repository import IUserRepository
from ..database.models import UserModel


class SQLAlchemyUserRepository(IUserRepository):
    """SQLAlchemyを使用したユーザーリポジトリ実装"""
    
    def __init__(self, session: AsyncSession):
        self._session = session
    
    async def save(self, user: User) -> User:
        """ユーザーを保存"""
        # TODO: TDDで実装してください
        # 1. ドメインエンティティをデータモデルに変換
        # 2. 新規作成または更新の判定
        # 3. データベースに保存
        # 4. 保存後のデータモデルをドメインエンティティに変換
        # 5. セッションコミット
        pass
    
    async def find_by_id(self, user_id: int) -> Optional[User]:
        """IDでユーザーを検索"""
        # TODO: TDDで実装してください
        # 1. SQLAlchemyでクエリ実行
        # 2. 結果をドメインエンティティに変換
        pass
    
    async def find_by_email(self, email: Email) -> Optional[User]:
        """メールアドレスでユーザーを検索"""
        # TODO: TDDで実装してください
        pass
    
    async def find_by_user_name(self, user_name: UserName) -> Optional[User]:
        """ユーザー名でユーザーを検索"""
        # TODO: TDDで実装してください
        pass
    
    async def exists_by_email(self, email: Email) -> bool:
        """メールアドレスの重複チェック"""
        # TODO: TDDで実装してください
        pass
    
    async def exists_by_user_name(self, user_name: UserName) -> bool:
        """ユーザー名の重複チェック"""
        # TODO: TDDで実装してください
        pass
    
    async def find_active_users(self) -> List[User]:
        """アクティブなユーザー一覧を取得"""
        # TODO: TDDで実装してください
        pass
    
    async def delete(self, user_id: int) -> bool:
        """ユーザーを削除"""
        # TODO: TDDで実装してください
        # - 論理削除（is_active = False）を推奨
        pass
    
    async def count_total_users(self) -> int:
        """総ユーザー数を取得"""
        # TODO: TDDで実装してください
        pass
    
    def _convert_to_domain_entity(self, user_model: UserModel) -> User:
        """データモデルをドメインエンティティに変換"""
        # TODO: TDDで実装してください
        # - UserModelからUserエンティティを作成
        # - バリューオブジェクトの復元
        pass
    
    def _convert_to_data_model(self, user: User) -> UserModel:
        """ドメインエンティティをデータモデルに変換"""
        # TODO: TDDで実装してください
        # - UserエンティティからUserModelを作成
        # - バリューオブジェクトの値を抽出
        pass