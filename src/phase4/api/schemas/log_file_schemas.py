"""
ログファイル API スキーマ

リクエスト・レスポンスのデータ構造を定義
"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional


class LogFileResponse(BaseModel):
    """ログファイルレスポンス"""
    
    id: Optional[int] = Field(description="ファイルID")
    file_name: str = Field(description="ファイル名")
    file_size_bytes: int = Field(description="ファイルサイズ（バイト）")
    file_size_display: str = Field(description="ファイルサイズ（表示用）")
    uploaded_at: datetime = Field(description="アップロード日時")
    uploaded_by: int = Field(description="アップロードユーザーID")
    is_log_file: bool = Field(description="ログファイルかどうか")
    can_be_analyzed: bool = Field(description="解析可能かどうか")
    file_extension: str = Field(description="ファイル拡張子")
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class LogFileListResponse(BaseModel):
    """ログファイル一覧レスポンス"""
    
    files: List[LogFileResponse] = Field(description="ファイル一覧")
    total_count: int = Field(description="総件数")
    total_size_bytes: int = Field(description="総サイズ（バイト）")


class UploadLogFileRequest(BaseModel):
    """ログファイルアップロードリクエスト"""
    
    file_name: str = Field(description="ファイル名")
    file_size: int = Field(description="ファイルサイズ")
    

class ErrorResponse(BaseModel):
    """エラーレスポンス"""
    
    error_code: str = Field(description="エラーコード")
    message: str = Field(description="エラーメッセージ")
    details: Optional[dict] = Field(default=None, description="詳細情報")