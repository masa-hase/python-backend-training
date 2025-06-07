"""
レポートAPI

Phase 3・4のレポート機能をデータベース対応版にアップグレード
"""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from ..auth.jwt_auth import AuthService
from ..database.database import get_database
from typing import Optional

router = APIRouter(prefix="/api/reports", tags=["レポート"])


@router.get("/logs/{file_id}/daily")
async def get_daily_report(
    file_id: int,
    date: Optional[str] = Query(None),
    current_user=Depends(AuthService.get_current_user),
    db: AsyncSession = Depends(get_database)
):
    """日次レポート（データベース版）"""
    # TODO: データベース対応版を実装してください
    pass


@router.get("/logs/{file_id}/performance")
async def get_performance_report(
    file_id: int,
    current_user=Depends(AuthService.get_current_user),
    db: AsyncSession = Depends(get_database)
):
    """パフォーマンスレポート（データベース版）"""
    # TODO: データベース対応版を実装してください
    pass