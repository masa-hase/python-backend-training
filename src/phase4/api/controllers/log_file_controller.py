"""
ログファイルコントローラー

【課題8】APIコントローラーをTDDで実装してください

コントローラーの責務:
- HTTPリクエストの受信
- DTOへの変換
- ユースケースの呼び出し
- HTTPレスポンスの生成
"""

from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, status
from typing import List
from ..schemas.log_file_schemas import LogFileResponse, LogFileListResponse
from ...application.use_cases.upload_log_file_use_case import UploadLogFileUseCase
from ...application.dto.upload_log_file_dto import UploadLogFileDto

router = APIRouter(prefix="/api/log-files", tags=["ログファイル"])


class LogFileController:
    """ログファイル操作のコントローラー"""
    
    def __init__(self, upload_use_case: UploadLogFileUseCase):
        self._upload_use_case = upload_use_case
    
    async def upload_log_file(
        self,
        file: UploadFile,
        current_user_id: int  # 認証から取得
    ) -> LogFileResponse:
        """ログファイルアップロード"""
        # TODO: TDDで実装してください
        
        # 1. リクエスト検証
        # 2. DTOへの変換
        # 3. ユースケース実行
        # 4. レスポンス変換
        # 5. エラーハンドリング
        
        pass
    
    async def get_user_log_files(
        self,
        current_user_id: int
    ) -> LogFileListResponse:
        """ユーザーのログファイル一覧取得"""
        # TODO: TDDで実装してください
        pass
    
    async def delete_log_file(
        self,
        file_id: int,
        current_user_id: int
    ) -> dict:
        """ログファイル削除"""
        # TODO: TDDで実装してください
        pass


# 依存性注入の設定（後で実装）
def get_upload_use_case() -> UploadLogFileUseCase:
    # TODO: DIコンテナから取得
    pass


# ルーターの設定
@router.post("/upload", response_model=LogFileResponse)
async def upload_log_file(
    file: UploadFile = File(...),
    current_user_id: int = 1,  # TODO: 認証から取得
    use_case: UploadLogFileUseCase = Depends(get_upload_use_case)
):
    controller = LogFileController(use_case)
    return await controller.upload_log_file(file, current_user_id)


@router.get("/", response_model=LogFileListResponse)
async def get_user_log_files(
    current_user_id: int = 1,  # TODO: 認証から取得
):
    # TODO: 実装
    pass


@router.delete("/{file_id}")
async def delete_log_file(
    file_id: int,
    current_user_id: int = 1,  # TODO: 認証から取得
):
    # TODO: 実装
    pass