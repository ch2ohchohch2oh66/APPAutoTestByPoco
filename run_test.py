#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/4/27
# Description: 测试运行入口

import sys
import os
import pytest
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # 输出到控制台
    ]
)
logger = logging.getLogger(__name__)

def main():
    """运行测试的主函数"""
    # 获取当前文件所在目录作为项目根目录
    project_root = os.path.dirname(os.path.abspath(__file__))
    
    # 准备pytest参数
    pytest_args = [
        '--confcutdir', project_root,  # 指定conftest.py所在目录
        '-vs',  # 详细输出
    ]
    
    # 如果命令行提供了额外参数，添加到pytest参数中
    if len(sys.argv) > 1:
        pytest_args.extend(sys.argv[1:])
    else:
        # 默认运行所有测试
        pytest_args.append('cases')
    
    logger.info(f"运行测试: pytest {' '.join(pytest_args)}")
    
    # 执行pytest
    return pytest.main(pytest_args)

if __name__ == "__main__":
    sys.exit(main()) 