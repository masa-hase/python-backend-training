"""
アサーション（assert文）の練習

様々な種類のアサーションを練習します。
"""


def test_equality():
    """等価性のテスト"""
    # 数値の等価性
    assert 42 == 42
    assert 3.14 == 3.14
    
    # 文字列の等価性
    assert "hello" == "hello"
    assert "Hello".lower() == "hello"
    
    # リストの等価性
    assert [1, 2, 3] == [1, 2, 3]
    assert [] == []
    
    # 辞書の等価性
    assert {"a": 1, "b": 2} == {"b": 2, "a": 1}
    
    # 不等価性
    assert 1 != 2
    assert "hello" != "world"
    assert [1, 2] != [1, 2, 3]


def test_truthiness():
    """真偽値のテスト"""
    # 真の値
    assert True
    assert 1
    assert "hello"
    assert [1, 2, 3]
    assert {"key": "value"}
    
    # 偽の値
    assert not False
    assert not 0
    assert not ""
    assert not []
    assert not {}
    assert not None
    
    # 条件式
    x = 10
    assert x > 5
    assert x < 20
    assert 5 < x < 20


def test_comparisons():
    """比較のテスト"""
    # 数値の比較
    assert 5 > 3
    assert 10 >= 10
    assert 2 < 5
    assert 7 <= 7
    
    # 文字列の比較（辞書式順序）
    assert "apple" < "banana"
    assert "zebra" > "aardvark"
    
    # リストの長さ比較
    list1 = [1, 2, 3]
    list2 = [4, 5]
    assert len(list1) > len(list2)
    
    # 複合条件
    x = 15
    assert 10 < x < 20
    assert x >= 10 and x <= 20


def test_membership():
    """包含関係のテスト"""
    # リスト内の要素
    fruits = ["apple", "banana", "orange"]
    assert "apple" in fruits
    assert "grape" not in fruits
    
    # 文字列内の部分文字列
    text = "Hello, World!"
    assert "Hello" in text
    assert "World" in text
    assert "Python" not in text
    
    # 辞書のキー
    data = {"name": "Alice", "age": 30}
    assert "name" in data
    assert "email" not in data
    
    # 集合の要素
    numbers = {1, 2, 3, 4, 5}
    assert 3 in numbers
    assert 10 not in numbers


def test_types():
    """型チェックのテスト"""
    # 基本的な型チェック
    assert isinstance(42, int)
    assert isinstance(3.14, float)
    assert isinstance("hello", str)
    assert isinstance([1, 2, 3], list)
    assert isinstance({"a": 1}, dict)
    assert isinstance(True, bool)
    
    # 型が違うことを確認
    assert not isinstance("42", int)
    assert not isinstance(42, str)
    
    # 複数の型をチェック
    value = 10
    assert isinstance(value, (int, float))  # int または float
    
    # None のチェック
    result = None
    assert result is None
    assert result is not False
    assert result is not 0