"""
ResponseTime バリューオブジェクト

レスポンス時間を表すバリューオブジェクト
"""

from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True) 
class ResponseTime:
    """レスポンス時間を表すバリューオブジェクト"""
    
    milliseconds: int
    
    # 閾値定数
    FAST_THRESHOLD_MS: ClassVar[int] = 100
    SLOW_THRESHOLD_MS: ClassVar[int] = 1000
    
    def __post_init__(self):
        """バリデーション"""
        # TODO: TDDで実装してください
        pass
    
    def is_fast(self) -> bool:
        """高速なレスポンスか判定"""
        # TODO: TDDで実装してください
        pass
    
    def is_slow(self) -> bool:
        """低速なレスポンスか判定"""
        # TODO: TDDで実装してください
        pass
    
    def to_seconds(self) -> float:
        """秒単位に変換"""
        # TODO: TDDで実装してください
        pass
    
    def get_performance_category(self) -> str:
        """パフォーマンスカテゴリ取得"""
        # TODO: TDDで実装してください
        # "fast", "normal", "slow", "very_slow"
        pass