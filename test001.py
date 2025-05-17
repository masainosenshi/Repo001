"""
テキストファイル内の単語の出現頻度をカウントするスクリプトaa。
"""

import argparse
import re
from collections import Counter
from typing import List, Dict

def count_words_in_file(filepath: str) -> Dict[str, int]:
    """
    指定されたファイルパスのテキストファイルを読み込み、単語の出現頻度をカウントします。

    Args:
        filepath: テキストファイルのパス。

    Returns:
        単語をキー、出現回数を値とする辞書。

    Raises:
        FileNotFoundError: 指定されたファイルが見つからない場合。
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            # 単語を抽出 (英数字、ひらがな、カタカナを単語として認識)
            words = re.findall(r'\b[\w\u3040-\u309f\u30a0-\u30ff]+\b', text)
            return Counter(words)
    except FileNotFoundError:
        print(f"エラー: ファイル '{filepath}' が見つかりませんでした。")
        raise

def display_word_counts(word_counts: Dict[str, int], top_n: int = 10):
    """
    単語の出現頻度を指定された数だけ表示します。

    Args:
        word_counts: 単語をキー、出現回数を値とする辞書。
        top_n: 表示する上位N件の単語数。
    """
    if not word_counts:
        print("カウントする単語がありませんでした。")
        return

    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    if not sorted_word_counts:
        print("カウントする単語がありませんでした。")
        return

    print(f"\n--- 上位 {top_n} 単語の出現頻度 ---")
    for word, count in sorted_word_counts[:top_n]:
        print(f"{word}: {count}")

def main():
    """
    スクリプトのエントリーポイント。コマンドライン引数を処理し、単語カウントを実行します。
    """
    parser = argparse.ArgumentParser(description="テキストファイル内の単語の出現頻度をカウントします。")
    parser.add_argument("filepath", help="カウント対象のテキストファイルへのパス")
    parser.add_argument("-n", "--top_n", type=int, default=10, help="表示する上位N件の単語数 (デフォルト: 10)")
    args = parser.parse_args()

    word_counts = count_words_in_file(args.filepath)
    display_word_counts(word_counts, args.top_n)

if __name__ == "__main__":
    main()
