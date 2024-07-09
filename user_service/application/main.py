from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title="User Service",
        docs_url="/api/docs",
        description="A microservice for managing user information and authentication.",
        debug=True,
    )

    return app
