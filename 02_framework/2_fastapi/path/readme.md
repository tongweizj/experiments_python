短答：**先啃官网，再用优质 YouTube 做“形象化加速”**。官网最准确、体系最稳；视频适合快速建立直觉与项目全貌，但容易过时。最佳做法是“文档当主线、视频当配菜”。

# 怎么选

* **官网 Tutorial（User Guide）**：权威、最新版，涵盖类型提示、依赖注入、验证、鉴权、测试、部署。
* **YouTube**：只选**2024年以后**更新、**提到 Pydantic v2** 的课程/项目实战。

  * ✅ 关键词：`pydantic v2`, `model_validate`, `Annotated dependencies`, `SQLModel/SQLAlchemy 2.0`
  * ❌ 过时信号：`BaseModel.parse_obj`、大量 `from pydantic import BaseSettings` 旧写法、SQLAlchemy 1.x session 用法

# 90 分钟入门顺序（今天就做）

1. **30 min 官网**：读并跟打

   * Path operations → 请求体（Body + Pydantic 模型）→ 校验&响应模型
2. **30 min 视频速览**：挑一部 1–2 小时的“从零到部署”课程，**先看 30 分钟**抓整体结构（路由/依赖/数据库/测试/容器化）。
3. **30 min 小练习**：实现一个 `/items/` 的增删改查（内存 dict 即可），写 3 个单元测试（`pytest`）。

# 你可以直接照抄的 2 周微课程（每天 45–60 分钟）

**Week 1（官方文档主线）**

* D1 路由与路径/查询参数；响应模型（含 `response_model`）
* D2 请求体 & Pydantic v2（`BaseModel`, `field_validators`）；错误处理
* D3 依赖注入（`Depends` + `Annotated`）；全局依赖与覆盖
* D4 中间件、CORS、背景任务、事件启动/关闭
* D5 测试（`TestClient`/`httpx` + `pytest`）；设置 `--reload` 与 `.env`
* D6–D7 小项目 V0：Todo API（内存版）→ V1：拆分 `routers/` + `deps/`，加 8–10 条测试

**Week 2（视频项目+数据库+安全）**

* D8 选一部**更新到 2024/2025**的视频课程，跟做数据库版（SQLModel 或 SQLAlchemy 2.0 + Alembic）
* D9 OAuth2 密码流或 JWT（FastAPI `Security`），路由分层 `api/v1`
* D10 错误与验证统一返回（异常处理器、自定义错误模型）
* D11–D12 文档与可观测性：OpenAPI 自定义、日志、请求时长中间件
* D13 Docker 打包（`uvicorn`/`gunicorn` + `uvloop`），本地容器跑通
* D14 小项目 V2：写 README（架构图/端点/测试覆盖/启动命令），录 3–5 分钟演示

# 学习时的“三件套”

1. **一体化模板仓库**（建议你的项目结构）

```
app/
  main.py
  api/v1/
    __init__.py
    items.py
  core/
    config.py  # pydantic-settings v2
    security.py
  models/     # SQLModel/SQLAlchemy
  deps/
tests/
  test_items.py
```

2. **测试先行**：每加一个端点就加 1–2 条 `pytest`；总时长控制在学习时间的 20–30%。
3. **对拍清单**：POST→GET→PUT→DELETE 的 happy path + 3 个边界（缺字段、类型错、权限不足）。

# 常见坑（避雷）

* **Pydantic 版本混乱**：确保教程&代码一致使用 v2（比如 `model_validate` 而非 `parse_obj`）。
* **依赖注入过度/过少**：可复用逻辑放依赖，业务内逻辑别塞太多到依赖里。
* **数据库会话泄漏**：用“每请求一个 session”的依赖工厂，测试时用事务回滚夹层。
* **只看不做**：每看完 10–15 分钟视频就**暂停并实现**一个端点或一段测试。

# 结论（给你一句话的决定规则）

> **先用官网建立“正确的骨架”，再挑一部“2024+、Pydantic v2”的 YouTube 项目来长肌肉。**
> 视频只用来加速理解与实战，**总时长不超过你学习时间的 40%**；其余时间在写代码和写测试。

如果你愿意，我可以按这个 2 周大纲，直接给你一个**可克隆的 FastAPI 学习仓库骨架**（含 `poetry/uv`、`pytest`、样例路由与测试、Dockerfile、Makefile），今天就能开敲。
