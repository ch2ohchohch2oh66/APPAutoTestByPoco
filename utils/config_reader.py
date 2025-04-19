#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/20
# Description: 配置文件读取工具

import os
import yaml

class ConfigReader:
    """配置文件读取类"""
    
    @staticmethod
    def read_yaml(file_path):
        """读取YAML配置文件
        
        Args:
            file_path: YAML文件路径
            
        Returns:
            dict: 配置文件内容
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"配置文件 {file_path} 不存在")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                config = yaml.safe_load(f)
                return config
            except yaml.YAMLError as e:
                raise ValueError(f"解析YAML文件 {file_path} 失败: {e}")
    
    @staticmethod
    def get_env_config(env='Prd'):
        """获取环境配置
        
        Args:
            env: 环境名称，默认为Prd
            
        Returns:
            dict: 环境配置
        """
        # 获取当前文件所在目录的上级目录（项目根目录）
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(project_root, 'configs', 'env', f'Config_{env}.yaml')
        
        return ConfigReader.read_yaml(config_path)
    
    @staticmethod
    def get_meeting_number(env='Prd'):
        """获取会议号
        
        Args:
            env: 环境名称，默认为Prd
            
        Returns:
            str: 会议号
        """
        config = ConfigReader.get_env_config(env)
        return str(config.get('conference', {}).get('meetingroom_number', ''))


if __name__ == '__main__':
    # 测试读取配置
    try:
        config = ConfigReader.get_env_config()
        print("配置文件内容:", config)
        meeting_number = ConfigReader.get_meeting_number()
        print("会议号:", meeting_number)
    except Exception as e:
        print(f"读取配置文件失败: {e}") 