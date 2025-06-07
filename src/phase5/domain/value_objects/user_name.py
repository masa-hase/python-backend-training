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
        if not self.value:
            raise ValueError("ユーザー名が空です")
        
        if not self.is_valid_length():
            raise ValueError(f"ユーザー名の長さは{self.MIN_LENGTH}文字以上{self.MAX_LENGTH}文字以下である必要があります")
        
        if not self.contains_only_allowed_chars():
            raise ValueError("ユーザー名に使用できない文字が含まれています。英数字、アンダースコア、ハイフンのみ使用可能です")
        
        if self.is_reserved_name():
            raise ValueError(f"ユーザー名 '{self.value}' はシステム予約語のため使用できません")
    
    def is_valid_length(self) -> bool:
        """長さが有効かチェック"""
        return self.MIN_LENGTH <= len(self.value) <= self.MAX_LENGTH
    
    def contains_only_allowed_chars(self) -> bool:
        """許可された文字のみを含むかチェック"""
        return bool(re.match(self.ALLOWED_PATTERN, self.value))
    
    def is_reserved_name(self) -> bool:
        """予約語かどうかチェック"""
        return self.value.lower() in self.RESERVED_NAMES
    
    @classmethod
    def suggest_alternative(cls, invalid_name: str) -> str:
        """無効なユーザー名に対して代替案を提案"""
        if not invalid_name:
            return "user123"
        
        # 特殊文字をアンダースコアに置換
        clean_name = re.sub(r'[^a-zA-Z0-9_-]', '_', invalid_name)
        
        # 連続したアンダースコアを一つに
        clean_name = re.sub(r'_+', '_', clean_name)
        
        # 前後のアンダースコアを除去
        clean_name = clean_name.strip('_')
        
        # 予約語の場合は接尾辞を追加
        if clean_name.lower() in cls.RESERVED_NAMES:
            clean_name += "_user"
        
        # 長さ調整
        if len(clean_name) < cls.MIN_LENGTH:
            clean_name += "123"
        elif len(clean_name) > cls.MAX_LENGTH:
            clean_name = clean_name[:cls.MAX_LENGTH]
        
        # まだ無効な場合はデフォルト名を返す
        try:
            cls(clean_name)
            return clean_name
        except ValueError:
            return "user123"