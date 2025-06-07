"""
TDD練習用ファイル

Phase 3の最初にTDDサイクルを体験するための練習です。

【練習1】計算機クラスをTDDで作成してください
"""

import pytest
from src.phase3.calculator import Calculator  # まだ存在しないクラス


class TestCalculator:
    """計算機のTDDテスト"""
    
    def test_add_two_numbers(self):
        """2つの数の足し算をテスト"""
        # Red: まず失敗するテストを書く
        calc = Calculator()
        result = calc.add(2, 3)
        assert result == 5
        
    def test_subtract_two_numbers(self):
        """2つの数の引き算をテスト"""
        # TODO: 引き算のテストを書いてください
        pass
    
    def test_multiply_two_numbers(self):
        """2つの数の掛け算をテスト"""
        # TODO: 掛け算のテストを書いてください
        pass
    
    def test_divide_two_numbers(self):
        """2つの数の割り算をテスト"""
        # TODO: 割り算のテストを書いてください
        pass
    
    def test_divide_by_zero(self):
        """ゼロ除算のテスト"""
        # TODO: ゼロ除算時の例外処理をテストしてください
        pass