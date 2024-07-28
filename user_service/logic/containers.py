from functools import lru_cache
from punq import Container, Scope

from user_service.infra.db.config import DBConfig
from user_service.infra.db.database import Database


@lru_cache(1)
def get_container() -> Container:
    return _init_container()


def _init_container() -> Container:
    container = Container()

    container.register(DBConfig, instance=DBConfig(), scope=Scope.singleton)

    # Database
    def init_database():
        config = container.resolve(DBConfig)
        return Database(url=config.full_database_url, ro_url=config.full_database_url)

    container.register(Database, factory=init_database, scope=Scope.singleton)

    return container
