"""
TDD練習用の計算機クラス

【課題1】TDDサイクルで実装してください

手順:
1. テストを実行して失敗することを確認（Red）
2. テストを通すための最小限のコードを書く（Green）
3. コードを整理・改善する（Refactor）
"""


class Calculator:
    """TDD練習用の計算機クラス"""
    
    def add(self, a: int, b: int) -> int:
        """足し算"""
        return a + b
    
    def subtract(self, a: int, b: int) -> int:
        """引き算"""
        return a - b
    
    def multiply(self, a: int, b: int) -> int:
        """掛け算"""
        return a * b
    
    def divide(self, a: int, b: int) -> float:
        """割り算"""
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a / b