"""
ログファイルアップロードユースケース

【課題6】ユースケースをTDDで実装してください

ユースケースの特徴:
- アプリケーション層のコンポーネント
- ビジネスルールの調整
- ドメインオブジェクトの協調
- トランザクションの境界
"""

from typing import Dict, Any
from datetime import datetime
from ..dto.upload_log_file_dto import UploadLogFileDto, UploadLogFileResultDto
from ...domain.entities.log_file import LogFile
from ...domain.value_objects.file_name import FileName
from ...domain.value_objects.file_size import FileSize
from ...domain.repositories.i_log_file_repository import ILogFileRepository


class UploadLogFileUseCase:
    """ログファイルアップロードのユースケース"""
    
    def __init__(self, log_file_repository: ILogFileRepository):
        self._log_file_repository = log_file_repository
    
    async def execute(self, dto: UploadLogFileDto) -> UploadLogFileResultDto:
        """ログファイルアップロードを実行"""
        try:
            # 1. バリデーション
            # ファイル名の検証（FileName作成時にバリデーション実行）
            file_name = FileName(dto.file_name)
            
            # ファイルサイズの検証（FileSize作成時にバリデーション実行）
            file_size = FileSize(dto.file_size)
            
            # 重複チェック
            if await self._log_file_repository.exists_by_name_and_user(dto.file_name, dto.user_id):
                return UploadLogFileResultDto(
                    file_id=0,
                    file_name=dto.file_name,
                    file_size=dto.file_size,
                    uploaded_at=datetime.now(),
                    success=False,
                    message="同名のファイルが既に存在します"
                )
            
            # 2. ドメインオブジェクトの作成
            log_file = LogFile(
                id=None,  # IDは保存時に自動生成
                file_name=file_name,
                file_size=file_size,
                uploaded_at=datetime.now(),
                uploaded_by=dto.user_id
            )
            
            # 3. ビジネスルールの適用
            if not log_file.can_be_analyzed():
                return UploadLogFileResultDto(
                    file_id=0,
                    file_name=dto.file_name,
                    file_size=dto.file_size,
                    uploaded_at=datetime.now(),
                    success=False,
                    message="ファイル形式またはサイズが解析に適していません"
                )
            
            # ユーザーの容量制限チェック（例：100MB制限）
            current_usage = await self._log_file_repository.get_total_size_by_user(dto.user_id)
            max_usage = 100 * 1024 * 1024  # 100MB
            
            if current_usage + dto.file_size > max_usage:
                return UploadLogFileResultDto(
                    file_id=0,
                    file_name=dto.file_name,
                    file_size=dto.file_size,
                    uploaded_at=datetime.now(),
                    success=False,
                    message="容量制限を超過しています"
                )
            
            # 4. 永続化
            saved_file = await self._log_file_repository.save(log_file)
            
            # 5. 結果の返却
            return UploadLogFileResultDto(
                file_id=saved_file.id,
                file_name=saved_file.file_name.value,
                file_size=saved_file.file_size.bytes,
                uploaded_at=saved_file.uploaded_at,
                success=True,
                message="ファイルアップロードが完了しました"
            )
            
        except ValueError as e:
            return UploadLogFileResultDto(
                file_id=0,
                file_name=dto.file_name,
                file_size=dto.file_size,
                uploaded_at=datetime.now(),
                success=False,
                message=f"バリデーションエラー: {str(e)}"
            )
        except Exception as e:
            return UploadLogFileResultDto(
                file_id=0,
                file_name=dto.file_name,
                file_size=dto.file_size,
                uploaded_at=datetime.now(),
                success=False,
                message=f"アップロードに失敗しました: {str(e)}"
            )