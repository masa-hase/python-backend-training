"""
ログ操作API

Phase 4の機能をデータベース対応版にアップグレード
"""

from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from ..auth.jwt_auth import AuthService
from ..database.database import get_database

router = APIRouter(prefix="/api/logs", tags=["ログ操作"])


@router.post("/upload")
async def upload_log_file(
    file: UploadFile = File(...),
    current_user=Depends(AuthService.get_current_user),
    db: AsyncSession = Depends(get_database)
):
    """ログファイルアップロード（認証必須）"""
    # TODO: データベース対応版を実装してください
    pass


@router.get("/")
async def get_uploaded_files(
    current_user=Depends(AuthService.get_current_user),
    db: AsyncSession = Depends(get_database)
):
    """ユーザーのログファイル一覧"""
    # TODO: データベース対応版を実装してください
    pass


@router.delete("/{file_id}")
async def delete_log_file(
    file_id: int,
    current_user=Depends(AuthService.get_current_user),
    db: AsyncSession = Depends(get_database)
):
    """ログファイル削除（所有者のみ）"""
    # TODO: データベース対応版を実装してください
    pass