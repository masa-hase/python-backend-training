"""
Email バリューオブジェクト

【課題1】メールアドレスのバリューオブジェクトをTDDで実装してください

バリューオブジェクトの特徴:
- 不変（イミュータブル）
- 等価性は値で判断
- 識別子を持たない
- バリデーションを含む
"""

from dataclasses import dataclass
import re
from typing import ClassVar


@dataclass(frozen=True)
class Email:
    """メールアドレスを表すバリューオブジェクト"""
    
    value: str
    
    # メールアドレスの正規表現パターン
    EMAIL_PATTERN: ClassVar[str] = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    MAX_LENGTH: ClassVar[int] = 254  # RFC 5321準拠
    
    def __post_init__(self):
        """初期化後のバリデーション"""
        # TODO: TDDでバリデーションを実装してください
        # - 空文字チェック
        # - 長さチェック
        # - 正規表現チェック
        # - 不正な場合はValueErrorを発生
        pass
    
    def get_local_part(self) -> str:
        """ローカル部（@より前）を取得"""
        # TODO: TDDで実装してください
        pass
    
    def get_domain_part(self) -> str:
        """ドメイン部（@より後）を取得"""
        # TODO: TDDで実装してください
        pass
    
    def is_corporate_email(self) -> bool:
        """企業メールアドレスかどうか判定（Gmail等を除外）"""
        # TODO: TDDで実装してください
        # フリーメールのドメインリストと照合
        pass
    
    @classmethod
    def is_valid_format(cls, email_string: str) -> bool:
        """メールアドレス形式が有効かチェック"""
        # TODO: TDDで実装してください
        pass