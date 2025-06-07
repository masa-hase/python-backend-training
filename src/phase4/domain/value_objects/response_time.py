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
        if self.milliseconds < 0:
            raise ValueError("レスポンス時間は0以上である必要があります")
        if self.milliseconds > 60000:  # 60秒以上は異常
            raise ValueError("レスポンス時間が異常に長いです")
    
    def is_fast(self) -> bool:
        """高速なレスポンスか判定"""
        return self.milliseconds < self.FAST_THRESHOLD_MS
    
    def is_slow(self) -> bool:
        """低速なレスポンスか判定"""
        return self.milliseconds >= self.SLOW_THRESHOLD_MS
    
    def to_seconds(self) -> float:
        """秒単位に変換"""
        return self.milliseconds / 1000.0
    
    def get_performance_category(self) -> str:
        """パフォーマンスカテゴリ取得"""
        if self.milliseconds < self.FAST_THRESHOLD_MS:
            return "fast"
        elif self.milliseconds < self.SLOW_THRESHOLD_MS:
            return "normal"
        elif self.milliseconds < 5000:
            return "slow"
        else:
            return "very_slow"