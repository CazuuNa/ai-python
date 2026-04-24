# 安装fastapi

## pip install fastapi
 - 最小化安装
 - 仅包含核心依赖，如starlette和pydantic
 - 不包含额外的工具或插件（如uvicorn--ASGI服务器）
 - 没有FastAPI CLI，无法使用fastapi dev
 - 没有httpx（测试客户端）都需要手动安装
 - 适用在生产环境镜像打包：减少体积增强安全性，依赖精细控制：可以根据需要安装必要的依赖，在容器内运行：服务器由外部管理

## pip install fastapi[standard]
 - 标准安装
 - 包含所有必要的依赖，如uvicorn、httpx等
 - 包含FastAPI CLI，用于使用fastapi dev
 - 包含httpx（用于 TestClient），jinja2 (模板)、python-multipart (表单) 和 email-validator (邮箱校验)
 - 适用在开发环境：方便调试和测试，无需额外配置
