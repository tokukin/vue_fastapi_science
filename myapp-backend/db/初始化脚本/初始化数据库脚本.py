import sqlite3
import os
import json
from typing import List, Dict  # 类型注解，增强代码可读性

# 1. 连接数据库（若不存在则创建，文件路径可自定义）
# 数据库文件会保存在当前目录，命名为 "mydatabase.db"
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)

conn = sqlite3.connect(os.path.join(current_dir, '../test.db'))

# 2. 创建游标对象
cursor = conn.cursor()

# 3. 执行 SQL：创建用户表（示例）
create_table_sql = """
CREATE TABLE IF NOT EXISTS "users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "username" TEXT NOT NULL UNIQUE,
    "email" TEXT NOT NULL UNIQUE,
    "hashed_password" TEXT NOT NULL,
    "is_active" BOOLEAN DEFAULT 1,
    "created_at" TIMESTAMP DEFAULT (datetime('now', 'localtime'))
)
"""
cursor.execute(create_table_sql)

# 4. 提交事务（创建表属于写操作，需提交）
conn.commit()

insert_users_sql = """
INSERT OR IGNORE INTO "users" (
    "username", 
    "email", 
    "hashed_password", 
    "is_active", 
    "created_at"
) VALUES 
    -- 普通用户1
    ('zhangsan', 'zhangsan@example.com', '$2b$12$9TQ2WJZJQ5Q5ZJZJQ5ZJZ.7QJZJQ5ZJZJQ5ZJZJQ5ZJZJQ5ZJZ', 1, datetime('now', 'localtime', '-5 days')),
    -- 普通用户2
    ('lisi', 'lisi@example.com', '$2b$12$8TQ2WJZJQ5Q5ZJZJQ5ZJZ.6QJZJQ5ZJZJQ5ZJZJQ5ZJZJQ5ZJZ', 1, datetime('now', 'localtime', '-3 days')),
    -- 管理员用户
    ('admin', 'admin@example.com', '$2b$12$7TQ2WJZJQ5Q5ZJZJQ5ZJZ.5QJZJQ5ZJZJQ5ZJZJQ5ZJZJQ5ZJZ', 1, datetime('now', 'localtime', '-10 days')),
    -- 已禁用用户
    ('wangwu', 'wangwu@example.com', '$2b$12$6TQ2WJZJQ5Q5ZJZJQ5ZJZ.4QJZJQ5ZJZJQ5ZJZJQ5ZJZJQ5ZJZ', 0, datetime('now', 'localtime', '-1 days')),
    -- 新注册用户
    ('zhaoliu', 'zhaoliu@example.com', '$2b$12$5TQ2WJZJQ5Q5ZJZJQ5ZJZ.3QJZJQ5ZJZJQ5ZJZJQ5ZJZJQ5ZJZ', 1, datetime('now', 'localtime'));
"""
cursor.execute(insert_users_sql)

# 4. 提交事务（插入数据属于写操作，需提交）
conn.commit()

create_table_sql = """
CREATE TABLE IF NOT EXISTS chemical_elements (
    "number" INTEGER PRIMARY KEY, -- 原子序数，元素的唯一标识
    symbol TEXT NOT NULL, -- 元素符号，如H、O等
    chineseName TEXT NOT NULL, -- 元素中文名称
    englishName TEXT NOT NULL, -- 元素英文名称
    weight REAL NOT NULL, -- 元素相对原子质量
    type TEXT NOT NULL, -- 元素类型，如nonmetal（非金属）等
    "group" INTEGER, -- 元素所在族，1-18
    period INTEGER NOT NULL, -- 元素所在周期，1-7
    electronConfig TEXT NOT NULL -- 电子排布式，如1s¹
);



"""

cursor.execute(create_table_sql)

# 4. 提交事务（创建表属于写操作，需提交）
conn.commit()
'''
sql_index = """
CREATE INDEX idx_symbol ON chemical_elements(symbol);
CREATE INDEX idx_type ON chemical_elements(type);
CREATE INDEX idx_group_period ON chemical_elements("group", period);
"""
cursor.executemany(sql_index)
conn.commit()

'''


# 拼接文件绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "元素周期表原始数据")

try:
    with open(file_path, "r", encoding="utf-8") as file:
        # 解析 JSON 数据为 Python 列表（包含字典）
        elements: List[Dict] = json.load(file)

    print(f"成功读取 {len(elements)} 种元素：")

    data = [
    (
        elem["number"], elem["symbol"], elem["chineseName"], elem["englishName"],
        elem["weight"], elem["type"], elem["group"], elem["period"], elem["electronConfig"]
    ) for elem in elements
]
    
    insert_sql = """
INSERT INTO chemical_elements (
    "number", symbol, chineseName, englishName, 
    weight, type, "group", period, electronConfig
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
"""
    cursor.executemany(insert_sql, data)
    conn.commit()
    print(f"成功插入 {len(data)} 条记录")

except FileNotFoundError:
    print(f"文件 '{file_path}' 不存在")
except json.JSONDecodeError as e:
    print(f"JSON 格式错误：{e}（请检查文件是否符合修正后的格式）")
except Exception as e:
    print(f"错误：{e}")

# 5. 关闭连接
conn.close()
print("数据库连接已关闭")
