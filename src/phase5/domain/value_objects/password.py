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
        # バリデーション実行
        if not cls.validate_password_requirements(plain_password):
            raise ValueError("パスワードが要件を満たしていません")
        
        # bcryptでハッシュ化
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
        
        return cls(hashed_value=hashed.decode('utf-8'))
    
    @classmethod
    def create_from_hash(cls, hashed_password: str) -> 'Password':
        """ハッシュ化済みパスワードからPasswordオブジェクトを作成"""
        if not hashed_password:
            raise ValueError("ハッシュ値が空です")
        return cls(hashed_value=hashed_password)
    
    def verify(self, plain_password: str) -> bool:
        """平文パスワードがこのパスワードと一致するかチェック"""
        if not plain_password:
            return False
        try:
            return bcrypt.checkpw(plain_password.encode('utf-8'), self.hashed_value.encode('utf-8'))
        except Exception:
            return False
    
    @classmethod
    def validate_password_requirements(cls, plain_password: str) -> bool:
        """パスワード要件をチェック"""
        if not plain_password:
            return False
        
        # 長さチェック
        if len(plain_password) < cls.MIN_LENGTH or len(plain_password) > cls.MAX_LENGTH:
            return False
        
        # 禁止パスワードチェック
        if plain_password.lower() in cls.FORBIDDEN_PASSWORDS:
            return False
        
        # 文字種チェック
        has_upper = bool(re.search(r'[A-Z]', plain_password))
        has_lower = bool(re.search(r'[a-z]', plain_password))
        has_digit = bool(re.search(r'\d', plain_password))
        has_symbol = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', plain_password))
        
        return has_upper and has_lower and has_digit and has_symbol
    
    @classmethod
    def get_password_strength(cls, plain_password: str) -> str:
        """パスワード強度を返す（弱い・普通・強い）"""
        if not cls.validate_password_requirements(plain_password):
            return "弱い"
        
        score = 0
        
        # 長さのスコア
        if len(plain_password) >= 12:
            score += 2
        elif len(plain_password) >= 10:
            score += 1
        
        # 文字種のスコア
        if re.search(r'[A-Z]', plain_password):
            score += 1
        if re.search(r'[a-z]', plain_password):
            score += 1
        if re.search(r'\d', plain_password):
            score += 1
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', plain_password):
            score += 1
        
        # 繰り返しパターンのペナルティ
        if re.search(r'(.)\1{2,}', plain_password):  # 同じ文字が3回以上
            score -= 1
        
        if score >= 5:
            return "強い"
        elif score >= 3:
            return "普通"
        else:
            return "弱い"