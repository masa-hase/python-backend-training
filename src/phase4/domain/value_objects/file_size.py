"""
FileSize バリューオブジェクト

ファイルサイズを表すバリューオブジェクト
"""

from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class FileSize:
    """ファイルサイズを表すバリューオブジェクト"""
    
    bytes: int
    
    # サイズ制限の定数
    MAX_SIZE_BYTES: ClassVar[int] = 10 * 1024 * 1024  # 10MB
    MIN_SIZE_BYTES: ClassVar[int] = 1
    
    def __post_init__(self):
        """バリデーション"""
        if self.bytes < self.MIN_SIZE_BYTES:
            raise ValueError(f"ファイルサイズは{self.MIN_SIZE_BYTES}バイト以上である必要があります")
        if self.bytes > self.MAX_SIZE_BYTES:
            raise ValueError(f"ファイルサイズは{self.MAX_SIZE_BYTES}バイト以下である必要があります")
    
    def to_kb(self) -> float:
        """KB単位に変換"""
        return self.bytes / 1024
    
    def to_mb(self) -> float:
        """MB単位に変換"""
        return self.bytes / (1024 * 1024)
    
    def is_large(self) -> bool:
        """大きなファイルか判定（1MB以上）"""
        return self.bytes >= 1024 * 1024
    
    def can_be_processed(self) -> bool:
        """処理可能なサイズか判定"""
        return self.bytes <= self.MAX_SIZE_BYTES
    
    def __str__(self) -> str:
        """人間が読みやすい形式で表示"""
        if self.bytes < 1024:
            return f"{self.bytes} B"
        elif self.bytes < 1024 * 1024:
            return f"{self.to_kb():.1f} KB"
        else:
            return f"{self.to_mb():.1f} MB"