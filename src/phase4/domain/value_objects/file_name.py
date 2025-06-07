"""
FileName バリューオブジェクト

【課題2】DDDのバリューオブジェクトをTDDで実装してください

バリューオブジェクトの特徴:
- 不変（イミュータブル）
- 等価性は値で判断
- 識別子を持たない
- バリデーションを含む
"""

from dataclasses import dataclass
from typing import ClassVar
import re


@dataclass(frozen=True)
class FileName:
    """ファイル名を表すバリューオブジェクト"""
    
    value: str
    
    # クラス定数
    MAX_LENGTH: ClassVar[int] = 255
    ALLOWED_EXTENSIONS: ClassVar[set] = {'.log', '.txt', '.csv'}
    FORBIDDEN_CHARS: ClassVar[set] = {'<', '>', ':', '"', '|', '?', '*'}
    
    def __post_init__(self):
        """初期化後のバリデーション"""
        # TODO: TDDでバリデーションを実装してください
        pass
    
    def get_extension(self) -> str:
        """ファイル拡張子を取得"""
        # TODO: TDDで実装してください
        pass
    
    def get_base_name(self) -> str:
        """拡張子を除いたファイル名を取得"""
        # TODO: TDDで実装してください
        pass
    
    def is_log_file(self) -> bool:
        """ログファイルかどうか判定"""
        # TODO: TDDで実装してください
        pass
    
    @classmethod
    def create_safe_name(cls, unsafe_name: str) -> 'FileName':
        """安全なファイル名を生成"""
        # TODO: TDDで実装してください
        pass