## TODO

- [ ] 先创建基础结构，实现一个实体（如作者）的完整 CRUD
- [ ] 然后复制模式到其他两个实体
- [ ] 最后处理实体间的关系（如书籍与作者、出版社的关联）

## 图书管理 API 目录结构
```text
book_management_api/
├── main.py                 # 应用入口
├── requirements.txt        # 项目依赖
├── config.py              # 配置文件
├── database.py            # 数据库连接配置
├── models/                # 数据模型目录
│   ├── __init__.py
│   ├── author.py          # 作者模型
│   ├── book.py           # 书籍模型
│   └── publisher.py      # 出版社模型
├── schemas/               # Pydantic 模型目录
│   ├── __init__.py
│   ├── author.py         # 作者相关的请求/响应模型
│   ├── book.py          # 书籍相关的请求/响应模型
│   └── publisher.py     # 出版社相关的请求/响应模型
├── crud/                 # 数据库操作目录
│   ├── __init__.py
│   ├── author.py        # 作者的 CRUD 操作
│   ├── book.py         # 书籍的 CRUD 操作
│   └── publisher.py    # 出版社的 CRUD 操作
├── routers/              # API 路由目录
│   ├── __init__.py
│   ├── authors.py       # 作者相关路由
│   ├── books.py        # 书籍相关路由
│   └── publishers.py   # 出版社相关路由
└── tests/               # 测试目录
    ├── __init__.py
    ├── test_authors.py
    ├── test_books.py
    └── test_publishers.py
```