# coding: utf-8

import pkgutil
import inspect
from flask import Blueprint

def _get_blueprints():
    blueprints = []
    for module_loader, module_name, ispkg in pkgutil.iter_modules(__path__):
        if ispkg:
            continue
        else:
            controller_module = __import__("app.controller." + module_name)
            for name, obj in inspect.getmembers(controller_module):
                if isinstance(obj, Blueprint):
                    blueprints.append(obj)
    return blueprints

blueprints = _get_blueprints()




