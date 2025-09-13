#!/usr/bin/env python3
"""
工具使用示例演示
这个文件展示了如何在Python中实现类似的功能
"""

import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

class ToolsDemo:
    """演示四个工具的基本功能"""
    
    def __init__(self):
        self.workspace = "/workspace"
    
    # 1. 网络搜索功能示例
    def web_search_example(self, query):
        """模拟网络搜索功能"""
        print(f"搜索: {query}")
        # 实际应用中可以使用搜索API
        # 例如: Google Custom Search API, Bing Search API等
        search_url = f"https://api.example.com/search?q={query}"
        # response = requests.get(search_url)
        # return response.json()
        return f"搜索结果: 关于'{query}'的相关信息"
    
    # 2. 文件操作功能示例
    def file_operations_example(self):
        """演示文件操作"""
        # 创建文件
        file_path = os.path.join(self.workspace, "test_file.txt")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("这是一个测试文件\n")
            f.write(f"创建时间: {datetime.now()}\n")
        
        # 读取文件
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"文件内容:\n{content}")
        
        # 列出目录
        files = os.listdir(self.workspace)
        print(f"目录内容: {files}")
        
        return file_path
    
    # 3. PDF生成功能示例（需要安装reportlab）
    def pdf_generation_example(self):
        """演示PDF生成（伪代码）"""
        try:
            from reportlab.pdfgen import canvas
            from reportlab.lib.pagesizes import letter
            
            pdf_path = os.path.join(self.workspace, "example.pdf")
            c = canvas.Canvas(pdf_path, pagesize=letter)
            c.drawString(100, 750, "示例PDF文档")
            c.drawString(100, 730, "这是使用Python生成的PDF")
            c.drawString(100, 710, f"生成时间: {datetime.now()}")
            c.save()
            
            return pdf_path
        except ImportError:
            print("需要安装reportlab库: pip install reportlab")
            return None
    
    # 4. 网页抓取功能示例
    def web_scraping_example(self, url):
        """演示网页抓取"""
        try:
            # 发送HTTP请求
            response = requests.get(url)
            response.raise_for_status()
            
            # 解析HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 提取数据示例
            data = {
                'title': soup.find('title').text if soup.find('title') else '',
                'headings': [h.text for h in soup.find_all(['h1', 'h2', 'h3'])],
                'links': [a.get('href') for a in soup.find_all('a', href=True)][:10],
                'paragraphs': [p.text for p in soup.find_all('p')][:5]
            }
            
            return data
        except Exception as e:
            print(f"抓取失败: {e}")
            return None
    
    def run_all_demos(self):
        """运行所有演示"""
        print("=" * 50)
        print("工具使用演示")
        print("=" * 50)
        
        # 1. 网络搜索
        print("\n1. 网络搜索工具演示:")
        result = self.web_search_example("Python编程")
        print(result)
        
        # 2. 文件操作
        print("\n2. 文件操作工具演示:")
        file_path = self.file_operations_example()
        
        # 3. PDF生成
        print("\n3. PDF生成工具演示:")
        pdf_path = self.pdf_generation_example()
        if pdf_path:
            print(f"PDF已生成: {pdf_path}")
        
        # 4. 网页抓取
        print("\n4. 网页抓取工具演示:")
        print("示例: 抓取网页数据")
        # data = self.web_scraping_example("https://example.com")
        # if data:
        #     print(json.dumps(data, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    demo = ToolsDemo()
    demo.run_all_demos()