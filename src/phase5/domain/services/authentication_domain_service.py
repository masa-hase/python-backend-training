"""
認証ドメインサービス

【課題6】ドメインサービスをTDDで実装してください

ドメインサービスの特徴:
- 複数のエンティティ・バリューオブジェクトにまたがるロジック
- ステートレス
- ドメイン知識をカプセル化
"""

from typing import Optional
from ..entities.user import User
from ..value_objects.email import Email
from ..value_objects.password import Password
from ..value_objects.user_name import UserName
from ..repositories.i_user_repository import IUserRepository


class AuthenticationDomainService:
    """認証に関するドメインサービス"""
    
    def __init__(self, user_repository: IUserRepository):
        self._user_repository = user_repository
    
    async def can_register_user(self, email: Email, user_name: UserName) -> bool:
        """ユーザー登録が可能かチェック"""
        # TODO: TDDで実装してください
        # - メールアドレスの重複チェック
        # - ユーザー名の重複チェック
        # - その他のビジネスルール
        pass
    
    async def authenticate_user(self, email: Email, plain_password: str) -> Optional[User]:
        """ユーザー認証"""
        # TODO: TDDで実装してください
        # - メールアドレスでユーザー検索
        # - パスワード認証
        # - アクティブユーザーのみ認証
        # - ログイン記録の更新
        pass
    
    async def is_password_compromised(self, password: Password) -> bool:
        """パスワードが侵害されているかチェック"""
        # TODO: TDDで実装してください
        # - 一般的な侵害されたパスワードリストと照合
        # - 実際の実装では外部APIを使用することも
        pass
    
    async def suggest_strong_password(self) -> str:
        """強力なパスワードを提案"""
        # TODO: TDDで実装してください
        # - ランダムで安全なパスワード生成
        # - パスワード要件を満たす
        pass
    
    async def validate_user_uniqueness(self, email: Email, user_name: UserName, 
                                       exclude_user_id: Optional[int] = None) -> dict:
        """ユーザーの一意性を検証"""
        # TODO: TDDで実装してください
        # - メールアドレスとユーザー名の重複チェック
        # - 更新時は自分自身を除外
        # - 結果を辞書で返す（email_exists, username_exists）
        pass
    
    def calculate_password_strength_score(self, plain_password: str) -> int:
        """パスワード強度をスコア（0-100）で計算"""
        # TODO: TDDで実装してください
        # - 長さ、文字種、エントロピーなどを考慮
        # - 0-100のスコアで返す
        pass