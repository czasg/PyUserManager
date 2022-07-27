# coding: utf-8
import pywss
import sqlalchemy
import src.initialize
import src.api


def sqlalchemy_engine():
    return sqlalchemy.create_engine(
        "postgresql://scott:tiger@localhost/test",
        pool_size=3,
        pool_recycle=3600,
        pool_pre_ping=True,
        pool_use_lifo=True,
        echo_pool=True
    )


if __name__ == '__main__':
    app = pywss.App()
    engine = sqlalchemy_engine()
    src.initialize.Initialize(app, engine)
    app.run()
