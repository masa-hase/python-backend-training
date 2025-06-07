"""
モックログファイルリポジトリ

テスト・開発用のインメモリ実装
"""

from typing import List, Optional, Dict
from ...domain.entities.log_file import LogFile
from ...domain.repositories.i_log_file_repository import ILogFileRepository


class MockLogFileRepository(ILogFileRepository):
    """インメモリのモックリポジトリ"""
    
    def __init__(self):
        self._files: Dict[int, LogFile] = {}
        self._next_id = 1
    
    async def save(self, log_file: LogFile) -> LogFile:
        """ログファイルを保存"""
        if log_file.id is None:
            # 新規作成
            log_file.id = self._next_id
            self._next_id += 1
        
        self._files[log_file.id] = log_file
        return log_file
    
    async def find_by_id(self, file_id: int) -> Optional[LogFile]:
        """IDでログファイルを検索"""
        return self._files.get(file_id)
    
    async def find_by_user_id(self, user_id: int) -> List[LogFile]:
        """ユーザーIDでログファイル一覧を取得"""
        return [f for f in self._files.values() if f.uploaded_by == user_id]
    
    async def find_by_name_and_user(self, file_name: str, user_id: int) -> Optional[LogFile]:
        """ファイル名とユーザーIDでログファイルを検索"""
        for log_file in self._files.values():
            if log_file.file_name.value == file_name and log_file.uploaded_by == user_id:
                return log_file
        return None
    
    async def delete_by_id(self, file_id: int) -> bool:
        """IDでログファイルを削除"""
        if file_id in self._files:
            del self._files[file_id]
            return True
        return False
    
    async def get_total_size_by_user(self, user_id: int) -> int:
        """ユーザーの使用容量を取得"""
        user_files = await self.find_by_user_id(user_id)
        return sum(f.file_size.bytes for f in user_files)
    
    async def exists_by_name_and_user(self, file_name: str, user_id: int) -> bool:
        """同名ファイルが存在するかチェック"""
        result = await self.find_by_name_and_user(file_name, user_id)
        return result is not None