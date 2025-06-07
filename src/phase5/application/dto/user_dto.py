"""
ユーザー関連DTO

【課題7】データ転送オブジェクトをTDDで実装してください

DTOの特徴:
- レイヤー間のデータ転送
- シリアライゼーション/デシリアライゼーション
- バリデーション
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class RegisterUserDto:
    """ユーザー登録リクエストDTO"""
    
    user_name: str
    email: str
    password: str
    
    def validate(self) -> dict:
        """DTOレベルでのバリデーション"""
        # TODO: TDDで実装してください
        # - 必須フィールドチェック
        # - 基本的な形式チェック
        # - エラーメッセージを辞書で返す
        pass


@dataclass
class LoginUserDto:
    """ログインリクエストDTO"""
    
    email: str
    password: str
    
    def validate(self) -> dict:
        """DTOレベルでのバリデーション"""
        # TODO: TDDで実装してください
        pass


@dataclass
class UserResponseDto:
    """ユーザー情報レスポンスDTO"""
    
    id: int
    user_name: str
    email: str
    is_active: bool
    created_at: datetime
    last_login_at: Optional[datetime] = None
    
    @classmethod
    def from_entity(cls, user) -> 'UserResponseDto':
        """UserエンティティからDTOを作成"""
        # TODO: TDDで実装してください
        # - パスワードなどの機密情報は除外
        pass


@dataclass
class ChangePasswordDto:
    """パスワード変更リクエストDTO"""
    
    current_password: str
    new_password: str
    confirm_password: str
    
    def validate(self) -> dict:
        """DTOレベルでのバリデーション"""
        # TODO: TDDで実装してください
        # - 新しいパスワードと確認パスワードの一致チェック
        # - 現在のパスワードと新しいパスワードの相違チェック
        pass


@dataclass
class AuthTokenDto:
    """認証トークンレスポンスDTO"""
    
    access_token: str
    token_type: str
    expires_in: int
    user: UserResponseDto
    
    @classmethod
    def create(cls, access_token: str, expires_in: int, user_dto: UserResponseDto) -> 'AuthTokenDto':
        """認証トークンDTOを作成"""
        # TODO: TDDで実装してください
        pass