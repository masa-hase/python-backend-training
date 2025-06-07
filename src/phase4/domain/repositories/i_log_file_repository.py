"""
ログファイルリポジトリインターフェース

ドメイン層のリポジトリ抽象化
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.log_file import LogFile


class ILogFileRepository(ABC):
    """ログファイルリポジトリのインターフェース"""
    
    @abstractmethod
    async def save(self, log_file: LogFile) -> LogFile:
        """ログファイルを保存"""
        pass
    
    @abstractmethod
    async def find_by_id(self, file_id: int) -> Optional[LogFile]:
        """IDでログファイルを検索"""
        pass
    
    @abstractmethod
    async def find_by_user_id(self, user_id: int) -> List[LogFile]:
        """ユーザーIDでログファイル一覧を取得"""
        pass
    
    @abstractmethod
    async def find_by_name_and_user(self, file_name: str, user_id: int) -> Optional[LogFile]:
        """ファイル名とユーザーIDでログファイルを検索（重複チェック用）"""
        pass
    
    @abstractmethod
    async def delete_by_id(self, file_id: int) -> bool:
        """IDでログファイルを削除"""
        pass
    
    @abstractmethod
    async def get_total_size_by_user(self, user_id: int) -> int:
        """ユーザーの使用容量を取得"""
        pass
    
    @abstractmethod
    async def exists_by_name_and_user(self, file_name: str, user_id: int) -> bool:
        """同名ファイルが存在するかチェック"""
        pass