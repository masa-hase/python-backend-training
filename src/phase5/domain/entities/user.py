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
        # TODO: バリデーション・ビジネスルールを実装してください
        # - created_atが未来でないかチェック
        # - is_activeのデフォルト値設定
        pass
    
    def authenticate(self, plain_password: str) -> bool:
        """パスワード認証"""
        # TODO: TDDで実装してください
        # - アクティブユーザーのみ認証可能
        # - パスワードの検証
        pass
    
    def change_password(self, current_password: str, new_password: str) -> None:
        """パスワード変更"""
        # TODO: TDDで実装してください
        # - 現在のパスワード確認
        # - 新しいパスワードのバリデーション
        # - パスワード更新
        # - updated_at更新
        pass
    
    def update_email(self, new_email: Email) -> None:
        """メールアドレス更新"""
        # TODO: TDDで実装してください
        # - アクティブユーザーのみ更新可能
        # - updated_at更新
        pass
    
    def deactivate(self) -> None:
        """ユーザーを無効化"""
        # TODO: TDDで実装してください
        pass
    
    def activate(self) -> None:
        """ユーザーを有効化"""
        # TODO: TDDで実装してください
        pass
    
    def record_login(self) -> None:
        """ログイン記録"""
        # TODO: TDDで実装してください
        # - last_login_at更新
        pass
    
    def is_password_expired(self, max_days: int = 90) -> bool:
        """パスワードが期限切れかチェック"""
        # TODO: TDDで実装してください
        # - updated_atまたはcreated_atから計算
        pass
    
    def get_user_info(self) -> dict:
        """ユーザー情報を取得（パスワード除外）"""
        # TODO: TDDで実装してください
        pass