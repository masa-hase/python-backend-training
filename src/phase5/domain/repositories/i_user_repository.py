"""
ユーザーリポジトリインターフェース

【課題5】リポジトリパターンをTDDで実装してください

リポジトリパターンの特徴:
- データアクセスの抽象化
- ドメイン層とインフラ層の分離
- テスタビリティの向上
"""

from abc import ABC, abstractmethod
from typing import Optional, List
from ..entities.user import User
from ..value_objects.email import Email
from ..value_objects.user_name import UserName


class IUserRepository(ABC):
    """ユーザーリポジトリのインターフェース"""
    
    @abstractmethod
    async def save(self, user: User) -> User:
        """ユーザーを保存"""
        # TODO: TDDで実装してください
        # - 新規作成時はIDを生成
        # - 更新時は既存レコードを更新
        pass
    
    @abstractmethod
    async def find_by_id(self, user_id: int) -> Optional[User]:
        """IDでユーザーを検索"""
        # TODO: TDDで実装してください
        pass
    
    @abstractmethod
    async def find_by_email(self, email: Email) -> Optional[User]:
        """メールアドレスでユーザーを検索"""
        # TODO: TDDで実装してください
        pass
    
    @abstractmethod
    async def find_by_user_name(self, user_name: UserName) -> Optional[User]:
        """ユーザー名でユーザーを検索"""
        # TODO: TDDで実装してください
        pass
    
    @abstractmethod
    async def exists_by_email(self, email: Email) -> bool:
        """メールアドレスの重複チェック"""
        # TODO: TDDで実装してください
        pass
    
    @abstractmethod
    async def exists_by_user_name(self, user_name: UserName) -> bool:
        """ユーザー名の重複チェック"""
        # TODO: TDDで実装してください
        pass
    
    @abstractmethod
    async def find_active_users(self) -> List[User]:
        """アクティブなユーザー一覧を取得"""
        # TODO: TDDで実装してください
        pass
    
    @abstractmethod
    async def delete(self, user_id: int) -> bool:
        """ユーザーを削除"""
        # TODO: TDDで実装してください
        # - 物理削除または論理削除
        pass
    
    @abstractmethod
    async def count_total_users(self) -> int:
        """総ユーザー数を取得"""
        # TODO: TDDで実装してください
        pass