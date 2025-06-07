"""
JWT認証機能

【課題3】JWT認証をTDDで実装してください
"""

from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = "your-secret-key-here"  # 本番では環境変数から取得
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()


class AuthService:
    """認証サービス"""
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """パスワード検証"""
        # TODO: TDDで実装してください
        pass
    
    @staticmethod
    def get_password_hash(password: str) -> str:
        """パスワードハッシュ化"""
        # TODO: TDDで実装してください
        pass
    
    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
        """アクセストークン生成"""
        # TODO: TDDで実装してください
        pass
    
    @staticmethod
    def verify_token(token: str) -> dict:
        """トークン検証"""
        # TODO: TDDで実装してください
        pass
    
    @staticmethod
    async def get_current_user(credentials: HTTPAuthorizationCredentials = None):
        """現在のユーザーを取得"""
        # TODO: TDDで実装してください
        pass