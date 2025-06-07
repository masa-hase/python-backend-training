"""
ログファイルアップロード用のDTO

【課題7】DTOを定義してください

DTOの特徴:
- データ転送オブジェクト
- レイヤー間のデータ受け渡し
- シリアライゼーション対応
"""

from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class UploadLogFileDto:
    """ログファイルアップロードリクエストDTO"""
    
    file_name: str
    file_content: bytes
    file_size: int
    user_id: int
    content_type: Optional[str] = None


@dataclass
class UploadLogFileResultDto:
    """ログファイルアップロード結果DTO"""
    
    file_id: int
    file_name: str
    file_size: int
    uploaded_at: datetime
    success: bool
    message: str