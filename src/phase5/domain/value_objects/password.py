"""
Password バリューオブジェクト

【課題2】パスワードのバリューオブジェクトをTDDで実装してください

セキュリティ要件:
- 最小8文字、最大128文字
- 大文字・小文字・数字・記号を含む
- 一般的なパスワードは禁止
- ハッシュ化機能
"""

from dataclasses import dataclass
from typing import ClassVar
import re
import bcrypt


@dataclass(frozen=True)
class Password:
    """パスワードを表すバリューオブジェクト"""
    
    hashed_value: str  # ハッシュ化された値のみ保持
    
    # パスワード要件
    MIN_LENGTH: ClassVar[int] = 8
    MAX_LENGTH: ClassVar[int] = 128
    
    # 禁止パスワードリスト（実際はもっと多い）
    FORBIDDEN_PASSWORDS: ClassVar[set] = {
        'password', '12345678', 'qwerty123', 'admin123',
        'password123', '87654321', '11111111'
    }
    
    @classmethod
    def create_from_plain(cls, plain_password: str) -> 'Password':
        """平文パスワードからPasswordオブジェクトを作成"""
        # TODO: TDDで実装してください
        # 1. バリデーション実行
        # 2. bcryptでハッシュ化
        # 3. Passwordオブジェクト作成
        pass
    
    @classmethod
    def create_from_hash(cls, hashed_password: str) -> 'Password':
        """ハッシュ化済みパスワードからPasswordオブジェクトを作成"""
        # TODO: TDDで実装してください
        pass
    
    def verify(self, plain_password: str) -> bool:
        """平文パスワードがこのパスワードと一致するかチェック"""
        # TODO: TDDで実装してください
        pass
    
    @classmethod
    def validate_password_requirements(cls, plain_password: str) -> bool:
        """パスワード要件をチェック"""
        # TODO: TDDで実装してください
        # - 長さチェック
        # - 文字種チェック（大文字・小文字・数字・記号）
        # - 禁止パスワードチェック
        pass
    
    @classmethod
    def get_password_strength(cls, plain_password: str) -> str:
        """パスワード強度を返す（弱い・普通・強い）"""
        # TODO: TDDで実装してください
        pass