"""
LogFile エンティティ

【課題1】DDDのエンティティをTDDで実装してください

エンティティの特徴:
- 一意の識別子を持つ
- ライフサイクルを通じて同一性を保つ
- ビジネスルールを含む
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from ..value_objects.file_name import FileName
from ..value_objects.file_size import FileSize


@dataclass
class LogFile:
    """ログファイルエンティティ"""
    
    id: Optional[int]
    file_name: FileName
    file_size: FileSize
    uploaded_at: datetime
    uploaded_by: int  # ユーザーID
    
    def __post_init__(self):
        """初期化後の処理"""
        # ビジネスルールのバリデーション
        if self.uploaded_by <= 0:
            raise ValueError("ユーザーIDは1以上である必要があります")
        
        # アップロード日時のバリデーション
        if self.uploaded_at > datetime.now():
            raise ValueError("アップロード日時は未来の日時にできません")
    
    def is_owned_by(self, user_id: int) -> bool:
        """指定されたユーザーの所有ファイルかチェック"""
        return self.uploaded_by == user_id
    
    def can_be_analyzed(self) -> bool:
        """解析可能かチェック（ファイルサイズ、形式など）"""
        # ファイルサイズのチェック
        if not self.file_size.can_be_processed():
            return False
        
        # ファイル形式のチェック
        extension = self.file_name.get_extension()
        return extension in {'.log', '.txt', '.csv'}
    
    def get_file_info(self) -> dict:
        """ファイル情報を取得"""
        return {
            'id': self.id,
            'file_name': self.file_name.value,
            'file_size_bytes': self.file_size.bytes,
            'file_size_display': str(self.file_size),
            'uploaded_at': self.uploaded_at.isoformat(),
            'uploaded_by': self.uploaded_by,
            'is_log_file': self.file_name.is_log_file(),
            'can_be_analyzed': self.can_be_analyzed(),
            'file_extension': self.file_name.get_extension()
        }