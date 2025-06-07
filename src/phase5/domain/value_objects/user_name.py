"""
UserName バリューオブジェクト

【課題3】ユーザー名のバリューオブジェクトをTDDで実装してください
"""

from dataclasses import dataclass
from typing import ClassVar
import re


@dataclass(frozen=True)
class UserName:
    """ユーザー名を表すバリューオブジェクト"""
    
    value: str
    
    # ユーザー名の制約
    MIN_LENGTH: ClassVar[int] = 3
    MAX_LENGTH: ClassVar[int] = 50
    ALLOWED_PATTERN: ClassVar[str] = r'^[a-zA-Z0-9_-]+$'
    
    # 予約語（システムで使用するため禁止）
    RESERVED_NAMES: ClassVar[set] = {
        'admin', 'root', 'system', 'api', 'www', 'mail',
        'test', 'guest', 'anonymous', 'null', 'undefined'
    }
    
    def __post_init__(self):
        """初期化後のバリデーション"""
        # TODO: TDDでバリデーションを実装してください
        # - 空文字・None チェック
        # - 長さチェック
        # - 文字種チェック（英数字・アンダースコア・ハイフンのみ）
        # - 予約語チェック
        # - 不正な場合はValueErrorを発生
        pass
    
    def is_valid_length(self) -> bool:
        """長さが有効かチェック"""
        # TODO: TDDで実装してください
        pass
    
    def contains_only_allowed_chars(self) -> bool:
        """許可された文字のみを含むかチェック"""
        # TODO: TDDで実装してください
        pass
    
    def is_reserved_name(self) -> bool:
        """予約語かどうかチェック"""
        # TODO: TDDで実装してください
        pass
    
    @classmethod
    def suggest_alternative(cls, invalid_name: str) -> str:
        """無効なユーザー名に対して代替案を提案"""
        # TODO: TDDで実装してください
        # 例: 'admin' -> 'admin_user', 特殊文字を除去など
        pass