#!/usr/bin/env python3
"""
Unit tests for collect_ai_news.py
"""

import sys
import types
import unittest

if 'bs4' not in sys.modules:
    fake_bs4 = types.ModuleType('bs4')
    fake_bs4.BeautifulSoup = object
    sys.modules['bs4'] = fake_bs4

import collect_ai_news as can


class TestMarkdownGeneration(unittest.TestCase):
    """Test Traditional Chinese markdown output"""

    def test_generate_markdown_traditional_chinese(self):
        items = [
            {
                'title': 'Test AI Title',
                'url': 'https://example.com',
                'source': 'Example Source'
            }
        ]

        content = can.generate_markdown(items)

        self.assertIn('全球 AI 新聞每日摘要', content)
        self.assertIn('最新 AI 新聞標題', content)
        self.assertIn('**摘要**', content)
        self.assertIn('本則新聞重點為', content)
        self.assertIn('Test AI Title', content)

    def test_generate_markdown_uses_existing_summary(self):
        items = [
            {
                'title': 'Test AI Title',
                'url': 'https://example.com',
                'source': 'Example Source',
                'summary': '這是一段繁體中文摘要。'
            }
        ]

        content = can.generate_markdown(items)

        self.assertIn('這是一段繁體中文摘要。', content)


if __name__ == '__main__':
    unittest.main()
