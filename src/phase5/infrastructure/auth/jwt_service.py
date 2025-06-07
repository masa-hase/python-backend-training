"""
JWT認証サービス（インフラ層）

【課題14】JWT認証機能をTDDで実装してください

インフラ層の特徴:
- 外部ライブラリの使用
- 技術的な実装詳細
- 設定管理
"""

from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from jose import JWTError, jwt
from ...domain.entities.user import User


class JWTService:
    """JWT認証を担当するインフラサービス"""
    
    def __init__(self, secret_key: str, algorithm: str = "HS256", 
                 access_token_expire_minutes: int = 30):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.access_token_expire_minutes = access_token_expire_minutes
    
    def create_access_token(self, user: User, expires_delta: Optional[timedelta] = None) -> str:
        """アクセストークンを生成"""
        # TODO: TDDで実装してください
        # 1. トークンのペイロード作成
        # 2. 有効期限の設定
        # 3. JWTトークン生成
        pass
    
    def verify_token(self, token: str) -> Optional[Dict[str, Any]]:
        """トークンを検証"""
        # TODO: TDDで実装してください
        # 1. JWTトークンのデコード
        # 2. 署名検証
        # 3. 有効期限チェック
        # 4. ペイロードを返す
        pass
    
    def extract_user_id_from_token(self, token: str) -> Optional[int]:
        """トークンからユーザーIDを抽出"""
        # TODO: TDDで実装してください
        pass
    
    def is_token_expired(self, token: str) -> bool:
        """トークンが期限切れかチェック"""
        # TODO: TDDで実装してください
        pass
    
    def get_token_expiration_time(self, token: str) -> Optional[datetime]:
        """トークンの有効期限を取得"""
        # TODO: TDDで実装してください
        pass
    
    def create_token_payload(self, user: User) -> Dict[str, Any]:
        """トークンのペイロードを作成"""
        # TODO: TDDで実装してください
        # - ユーザーID、メールアドレス等を含める
        # - 機密情報は含めない
        pass