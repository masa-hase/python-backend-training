"""
アプリケーション設定

【課題8】環境変数を使った設定管理を実装してください
"""

from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """アプリケーション設定"""
    
    # データベース設定
    database_url: str = "sqlite+aiosqlite:///./app.db"
    
    # JWT設定
    secret_key: str = "your-secret-key-here"
    access_token_expire_minutes: int = 30
    
    # ログ設定
    log_level: str = "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # アプリケーション設定
    app_name: str = "ログ解析API"
    app_version: str = "2.0.0"
    debug: bool = False
    
    # TODO: その他の設定を追加
    
    class Config:
        env_file = ".env"


settings = Settings()