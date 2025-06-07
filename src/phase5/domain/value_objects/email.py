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
        if not self.value:
            raise ValueError("メールアドレスが空です")
        
        if len(self.value) > self.MAX_LENGTH:
            raise ValueError(f"メールアドレスが長すぎます。最大{self.MAX_LENGTH}文字です")
        
        if not re.match(self.EMAIL_PATTERN, self.value):
            raise ValueError("無効なメールアドレス形式です")
    
    def get_local_part(self) -> str:
        """ローカル部（@より前）を取得"""
        return self.value.split('@')[0]
    
    def get_domain_part(self) -> str:
        """ドメイン部（@より後）を取得"""
        return self.value.split('@')[1]
    
    def is_corporate_email(self) -> bool:
        """企業メールアドレスかどうか判定（Gmail等を除外）"""
        free_email_domains = {
            'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com',
            'yahoo.co.jp', 'icloud.com', 'aol.com', 'live.com'
        }
        domain = self.get_domain_part().lower()
        return domain not in free_email_domains
    
    @classmethod
    def is_valid_format(cls, email_string: str) -> bool:
        """メールアドレス形式が有効かチェック"""
        if not email_string or len(email_string) > cls.MAX_LENGTH:
            return False
        return bool(re.match(cls.EMAIL_PATTERN, email_string))