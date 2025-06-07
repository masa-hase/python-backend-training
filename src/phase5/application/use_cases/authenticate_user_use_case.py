"""
ユーザー認証ユースケース

【課題9】ユーザー認証のユースケースをTDDで実装してください
"""

from typing import Optional
from ..dto.user_dto import LoginUserDto, AuthTokenDto, UserResponseDto
from ...domain.entities.user import User
from ...domain.value_objects.email import Email
from ...domain.repositories.i_user_repository import IUserRepository
from ...domain.services.authentication_domain_service import AuthenticationDomainService


class AuthenticateUserUseCase:
    """ユーザー認証のユースケース"""
    
    def __init__(self, user_repository: IUserRepository, 
                 auth_domain_service: AuthenticationDomainService,
                 jwt_service):  # インフラ層のJWTサービス
        self._user_repository = user_repository
        self._auth_domain_service = auth_domain_service
        self._jwt_service = jwt_service
    
    async def execute(self, dto: LoginUserDto) -> Optional[AuthTokenDto]:
        """ユーザー認証を実行"""
        # TODO: TDDで実装してください
        
        # 1. DTOのバリデーション
        #    - 必須フィールドチェック
        
        # 2. メールアドレスのバリューオブジェクト化
        #    - Email バリューオブジェクト作成
        
        # 3. ドメインサービスで認証
        #    - メールアドレスとパスワードで認証
        #    - ログイン記録の更新
        
        # 4. JWTトークン生成
        #    - アクセストークン作成
        #    - 有効期限設定
        
        # 5. レスポンスDTOの作成
        #    - AuthTokenDto 作成
        #    - ユーザー情報とトークンを含む
        
        pass
    
    async def validate_login_data(self, dto: LoginUserDto) -> dict:
        """ログインデータのバリデーション"""
        # TODO: TDDで実装してください
        pass