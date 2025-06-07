"""
最初のテスト練習

Phase 2 の最初に学習するための基本的なテストです。
"""


def test_simple_addition():
    """最も基本的なテスト"""
    # テストの基本形
    result = 2 + 3
    assert result == 5
    
    # 複数のアサーション
    assert 1 + 1 == 2
    assert 10 - 5 == 5
    assert 3 * 4 == 12
    
    # より複雑な計算
    assert (2 + 3) * 4 == 20


def test_string_operations():
    """文字列操作のテスト"""
    # 文字列の基本操作
    text = "Hello, World!"
    assert len(text) == 13
    assert text.upper() == "HELLO, WORLD!"
    assert text.lower() == "hello, world!"
    
    # 文字列の分割
    words = text.split(", ")
    assert len(words) == 2
    assert words[0] == "Hello"
    assert words[1] == "World!"
    
    # 文字列の結合
    joined = " ".join(["Python", "is", "awesome"])
    assert joined == "Python is awesome"
    
    # 文字列の検索
    assert "World" in text
    assert "Python" not in text
    assert text.startswith("Hello")
    assert text.endswith("!")