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
        calc = Calculator()
        
        # 基本的な引き算
        assert calc.subtract(5, 3) == 2
        assert calc.subtract(10, 4) == 6
        
        # ゼロとの引き算
        assert calc.subtract(5, 0) == 5
        assert calc.subtract(0, 3) == -3
        
        # 負の数との引き算
        assert calc.subtract(-2, 3) == -5
        assert calc.subtract(5, -3) == 8
        assert calc.subtract(-5, -3) == -2
    
    def test_multiply_two_numbers(self):
        """2つの数の掛け算をテスト"""
        calc = Calculator()
        
        # 基本的な掛け算
        assert calc.multiply(3, 4) == 12
        assert calc.multiply(2, 5) == 10
        
        # ゼロとの掛け算
        assert calc.multiply(5, 0) == 0
        assert calc.multiply(0, 10) == 0
        
        # 1との掛け算
        assert calc.multiply(7, 1) == 7
        assert calc.multiply(1, 9) == 9
        
        # 負の数との掛け算
        assert calc.multiply(-3, 4) == -12
        assert calc.multiply(3, -4) == -12
        assert calc.multiply(-3, -4) == 12
    
    def test_divide_two_numbers(self):
        """2つの数の割り算をテスト"""
        calc = Calculator()
        
        # 基本的な割り算
        assert calc.divide(10, 2) == 5.0
        assert calc.divide(15, 3) == 5.0
        assert calc.divide(7, 2) == 3.5
        
        # 1での割り算
        assert calc.divide(8, 1) == 8.0
        
        # 負の数での割り算
        assert calc.divide(-10, 2) == -5.0
        assert calc.divide(10, -2) == -5.0
        assert calc.divide(-10, -2) == 5.0
    
    def test_divide_by_zero(self):
        """ゼロ除算のテスト"""
        calc = Calculator()
        
        # ゼロで割るとZeroDivisionErrorが発生することをテスト
        with pytest.raises(ZeroDivisionError) as exc_info:
            calc.divide(10, 0)
        
        # エラーメッセージをチェック
        assert str(exc_info.value) == "Division by zero is not allowed"
        
        # 負の数をゼロで割る場合もテスト
        with pytest.raises(ZeroDivisionError):
            calc.divide(-5, 0)