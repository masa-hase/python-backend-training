"""
認証API用Pydanticスキーマ

【課題15】APIスキーマをTDDで実装してください

Pydanticスキーマの特徴:
- リクエスト/レスポンスの型定義
- バリデーション
- シリアライゼーション
"""

from pydantic import BaseModel, EmailStr, Field, validator
from datetime import datetime
from typing import Optional


class RegisterRequest(BaseModel):
    """ユーザー登録リクエストスキーマ"""
    
    user_name: str = Field(..., min_length=3, max_length=50, description="ユーザー名")
    email: EmailStr = Field(..., description="メールアドレス")
    password: str = Field(..., min_length=8, max_length=128, description="パスワード")
    
    @validator('user_name')
    def validate_user_name(cls, v):
        """ユーザー名のバリデーション"""
        # TODO: TDDで実装してください
        # - 英数字・アンダースコア・ハイフンのみ
        # - 予約語チェック
        pass
    
    @validator('password')
    def validate_password(cls, v):
        """パスワードのバリデーション"""
        # TODO: TDDで実装してください
        # - 大文字・小文字・数字・記号を含む
        # - 一般的なパスワードの禁止
        pass


class LoginRequest(BaseModel):
    """ログインリクエストスキーマ"""
    
    email: EmailStr = Field(..., description="メールアドレス")
    password: str = Field(..., min_length=1, description="パスワード")


class ChangePasswordRequest(BaseModel):
    """パスワード変更リクエストスキーマ"""
    
    current_password: str = Field(..., min_length=1, description="現在のパスワード")
    new_password: str = Field(..., min_length=8, max_length=128, description="新しいパスワード")
    confirm_password: str = Field(..., min_length=8, max_length=128, description="新しいパスワード（確認）")
    
    @validator('confirm_password')
    def passwords_match(cls, v, values):
        """パスワード一致チェック"""
        # TODO: TDDで実装してください
        pass


class UserResponse(BaseModel):
    """ユーザー情報レスポンススキーマ"""
    
    id: int
    user_name: str
    email: str
    is_active: bool
    created_at: datetime
    last_login_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class AuthTokenResponse(BaseModel):
    """認証トークンレスポンススキーマ"""
    
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    user: UserResponse


class ErrorResponse(BaseModel):
    """エラーレスポンススキーマ"""
    
    error_code: str
    message: str
    details: Optional[dict] = None