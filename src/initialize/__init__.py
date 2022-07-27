# coding: utf-8
import pywss
import sqlalchemy

from ..api import RegisterRoute
from ..model import InitializeModel


def Initialize(app: pywss.App, engine: sqlalchemy.engine):
    InitializeModel(engine)
    RegisterRoute(app)
