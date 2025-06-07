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
        # TODO: バリデーション・ビジネスルールを実装してください
        pass
    
    def is_owned_by(self, user_id: int) -> bool:
        """指定されたユーザーの所有ファイルかチェック"""
        # TODO: TDDで実装してください
        pass
    
    def can_be_analyzed(self) -> bool:
        """解析可能かチェック（ファイルサイズ、形式など）"""
        # TODO: TDDで実装してください
        pass
    
    def get_file_info(self) -> dict:
        """ファイル情報を取得"""
        # TODO: TDDで実装してください
        pass