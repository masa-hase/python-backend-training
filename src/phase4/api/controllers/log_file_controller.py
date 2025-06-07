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
        try:
            # 1. リクエスト検証
            if not file.filename:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="ファイル名が指定されていません"
                )
            
            # ファイル内容を読み込み
            file_content = await file.read()
            file_size = len(file_content)
            
            # 2. DTOへの変換
            dto = UploadLogFileDto(
                file_name=file.filename,
                file_content=file_content,
                file_size=file_size,
                user_id=current_user_id,
                content_type=file.content_type
            )
            
            # 3. ユースケース実行
            result = await self._upload_use_case.execute(dto)
            
            # 4. レスポンス変換
            if not result.success:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=result.message
                )
            
            return LogFileResponse(
                id=result.file_id,
                file_name=result.file_name,
                file_size_bytes=result.file_size,
                file_size_display=f"{result.file_size / 1024:.1f} KB" if result.file_size < 1024*1024 else f"{result.file_size / (1024*1024):.1f} MB",
                uploaded_at=result.uploaded_at,
                uploaded_by=current_user_id,
                is_log_file=result.file_name.endswith('.log'),
                can_be_analyzed=True,  # 成功したファイルは解析可能
                file_extension=result.file_name.split('.')[-1] if '.' in result.file_name else ""
            )
            
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"アップロードに失敗しました: {str(e)}"
            )
    
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


# 依存性注入の設定
def get_upload_use_case() -> UploadLogFileUseCase:
    from ...infrastructure.repositories.mock_log_file_repository import MockLogFileRepository
    repository = MockLogFileRepository()
    return UploadLogFileUseCase(repository)


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