"""
User エンティティ

【課題4】ユーザーエンティティをTDDで実装してください

エンティティの特徴:
- 一意の識別子を持つ
- ライフサイクルを通じて同一性を保つ
- ビジネスルールを含む
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from ..value_objects.email import Email
from ..value_objects.password import Password
from ..value_objects.user_name import UserName


@dataclass
class User:
    """ユーザーエンティティ"""
    
    id: Optional[int]
    user_name: UserName
    email: Email
    password: Password
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    last_login_at: Optional[datetime] = None
    
    def __post_init__(self):
        """初期化後の処理"""
        # created_atが未来でないかチェック
        if self.created_at > datetime.now():
            raise ValueError("作成日時は未来の日時にできません")
        
        # updated_atがNoneの場合はcreated_atと同じに設定
        if self.updated_at is None:
            object.__setattr__(self, 'updated_at', self.created_at)
    
    def authenticate(self, plain_password: str) -> bool:
        """パスワード認証"""
        # アクティブユーザーのみ認証可能
        if not self.is_active:
            return False
        
        # パスワードの検証
        return self.password.verify(plain_password)
    
    def change_password(self, current_password: str, new_password: str) -> None:
        """パスワード変更"""
        # 現在のパスワード確認
        if not self.password.verify(current_password):
            raise ValueError("現在のパスワードが正しくありません")
        
        # 新しいパスワードのバリデーションと更新
        new_password_obj = Password.create_from_plain(new_password)
        object.__setattr__(self, 'password', new_password_obj)
        object.__setattr__(self, 'updated_at', datetime.now())
    
    def update_email(self, new_email: Email) -> None:
        """メールアドレス更新"""
        # アクティブユーザーのみ更新可能
        if not self.is_active:
            raise ValueError("非アクティブユーザーのメールアドレスは更新できません")
        
        object.__setattr__(self, 'email', new_email)
        object.__setattr__(self, 'updated_at', datetime.now())
    
    def deactivate(self) -> None:
        """ユーザーを無効化"""
        object.__setattr__(self, 'is_active', False)
        object.__setattr__(self, 'updated_at', datetime.now())
    
    def activate(self) -> None:
        """ユーザーを有効化"""
        object.__setattr__(self, 'is_active', True)
        object.__setattr__(self, 'updated_at', datetime.now())
    
    def record_login(self) -> None:
        """ログイン記録"""
        object.__setattr__(self, 'last_login_at', datetime.now())
    
    def is_password_expired(self, max_days: int = 90) -> bool:
        """パスワードが期限切れかチェック"""
        from datetime import timedelta
        
        # 最後のパスワード更新日時を取得
        last_update = self.updated_at if self.updated_at else self.created_at
        
        # 期限を計算
        expiry_date = last_update + timedelta(days=max_days)
        
        return datetime.now() > expiry_date
    
    def get_user_info(self) -> dict:
        """ユーザー情報を取得（パスワード除外）"""
        return {
            'id': self.id,
            'user_name': self.user_name.value,
            'email': self.email.value,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'last_login_at': self.last_login_at.isoformat() if self.last_login_at else None,
            'is_password_expired': self.is_password_expired()
        }