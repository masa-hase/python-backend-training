"""
パスワード変更ユースケース

【課題10】パスワード変更のユースケースをTDDで実装してください
"""

from ..dto.user_dto import ChangePasswordDto, UserResponseDto
from ...domain.entities.user import User
from ...domain.value_objects.password import Password
from ...domain.repositories.i_user_repository import IUserRepository
from ...domain.services.authentication_domain_service import AuthenticationDomainService


class ChangePasswordUseCase:
    """パスワード変更のユースケース"""
    
    def __init__(self, user_repository: IUserRepository,
                 auth_domain_service: AuthenticationDomainService):
        self._user_repository = user_repository
        self._auth_domain_service = auth_domain_service
    
    async def execute(self, user_id: int, dto: ChangePasswordDto) -> UserResponseDto:
        """パスワード変更を実行"""
        # TODO: TDDで実装してください
        
        # 1. DTOのバリデーション
        #    - 必須フィールドチェック
        #    - 新しいパスワードと確認パスワードの一致
        
        # 2. ユーザーの取得
        #    - 指定されたIDのユーザーを取得
        #    - 存在チェック・アクティブチェック
        
        # 3. 現在のパスワード確認
        #    - ユーザーエンティティで認証
        
        # 4. 新しいパスワードのバリデーション
        #    - Password バリューオブジェクト作成
        #    - ドメインサービスでの侵害チェック
        
        # 5. パスワード変更
        #    - ユーザーエンティティのパスワード変更
        
        # 6. 永続化
        #    - リポジトリでユーザー更新
        
        # 7. レスポンスDTOの作成
        
        pass
    
    async def validate_password_change_data(self, dto: ChangePasswordDto) -> dict:
        """パスワード変更データのバリデーション"""
        # TODO: TDDで実装してください
        pass