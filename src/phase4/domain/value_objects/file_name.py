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
        if not self.value:
            raise ValueError("ファイル名が空です")
        
        if len(self.value) > self.MAX_LENGTH:
            raise ValueError(f"ファイル名が長すぎます。最大{self.MAX_LENGTH}文字です")
        
        # 禁止文字のチェック
        for char in self.FORBIDDEN_CHARS:
            if char in self.value:
                raise ValueError(f"禁止文字 '{char}' が含まれています")
        
        # 空白文字のチェック
        if self.value.strip() != self.value:
            raise ValueError("ファイル名の前後に空白文字は使用できません")
        
        # 拡張子のチェック
        import os
        extension = os.path.splitext(self.value)[1].lower()
        if extension and extension not in self.ALLOWED_EXTENSIONS:
            raise ValueError(f"サポートされていないファイル形式です: {extension}")
    
    def get_extension(self) -> str:
        """ファイル拡張子を取得"""
        import os
        return os.path.splitext(self.value)[1].lower()
    
    def get_base_name(self) -> str:
        """拡張子を除いたファイル名を取得"""
        import os
        return os.path.splitext(self.value)[0]
    
    def is_log_file(self) -> bool:
        """ログファイルかどうか判定"""
        extension = self.get_extension()
        return extension == '.log'
    
    @classmethod
    def create_safe_name(cls, unsafe_name: str) -> 'FileName':
        """安全なファイル名を生成"""
        if not unsafe_name:
            raise ValueError("ファイル名が空です")
        
        # 禁止文字をアンダースコアに置換
        safe_name = unsafe_name
        for char in cls.FORBIDDEN_CHARS:
            safe_name = safe_name.replace(char, '_')
        
        # 空白文字をアンダースコアに置換
        safe_name = re.sub(r'\s+', '_', safe_name)
        
        # 連続したアンダースコアを一つに
        safe_name = re.sub(r'_+', '_', safe_name)
        
        # 前後のアンダースコアを除去
        safe_name = safe_name.strip('_')
        
        # 長さの制限
        if len(safe_name) > cls.MAX_LENGTH:
            import os
            base, ext = os.path.splitext(safe_name)
            max_base_length = cls.MAX_LENGTH - len(ext)
            safe_name = base[:max_base_length] + ext
        
        # 拡張子がない場合は.logを追加
        if not safe_name.endswith(tuple(cls.ALLOWED_EXTENSIONS)):
            safe_name += '.log'
        
        return cls(safe_name)