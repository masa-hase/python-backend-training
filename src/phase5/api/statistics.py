"""
統計API

Phase 3・4の統計機能をデータベース対応版にアップグレード
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..auth.jwt_auth import AuthService
from ..database.database import get_database

router = APIRouter(prefix="/api/statistics", tags=["統計"])


@router.get("/logs/{file_id}/hourly")
async def get_hourly_statistics(
    file_id: int,
    current_user=Depends(AuthService.get_current_user),
    db: AsyncSession = Depends(get_database)
):
    """時間帯別統計（データベース版）"""
    # TODO: データベース対応版を実装してください
    pass


@router.get("/logs/{file_id}/response-time")
async def get_response_time_statistics(
    file_id: int,
    current_user=Depends(AuthService.get_current_user),
    db: AsyncSession = Depends(get_database)
):
    """レスポンス時間統計（データベース版）"""
    # TODO: データベース対応版を実装してください
    pass


@router.get("/logs/{file_id}/errors")
async def get_error_statistics(
    file_id: int,
    current_user=Depends(AuthService.get_current_user),
    db: AsyncSession = Depends(get_database)
):
    """エラー統計（データベース版）"""
    # TODO: データベース対応版を実装してください
    pass