#!/usr/bin/env python3
"""
Test script to check Python code syntax in Quarto files.
"""
import ast
import re
import sys


def test_multiprocessing_syntax():
    """Test the multiprocessing chapter for syntax errors."""
    print("Testing multiprocessing chapter syntax...")

    try:
        with open('en/book/11-multiprocessing.qmd') as f:
            content = f.read()

        # Find Python code blocks
        pattern = r'```\{python\}(.*?)```'
        blocks = re.findall(pattern, content, re.DOTALL)

        print(f"Found {len(blocks)} Python code blocks")

        for i, block in enumerate(blocks, 1):
            if block.strip():
                try:
                    ast.parse(block.strip())
                    print(f"  Block {i}: OK")
                except SyntaxError as e:
                    print(f"  Block {i}: SYNTAX ERROR - {e}")
                    print(f"    Block content preview: {block.strip()[:100]}...")
                    return False

        print("All Python code blocks passed syntax check!")
        return True

    except Exception as e:
        print(f"Error reading file: {e}")
        return False

if __name__ == "__main__":
    success = test_multiprocessing_syntax()
    sys.exit(0 if success else 1)
