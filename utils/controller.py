#coding: utf-8

from werkzeug.exceptions import HTTPException

class InValidException(Exception):
    pass


def validate(check_func, invalid_status=None):
    invalid_status = 403 if invalid_status == None else invalid_status
    def deco(method_func):
        def wrapper(self, *args, **kwd):
            try:
                result = check_func(*args, **kwd)
                if not result:
                    raise InValidException("InValidException: %s is invalid." % check_func.__name__, invalid_status) 
            except InValidException as e: 
                raise e
            except HTTPException as e:
                raise e
            except Exception as e:
                raise InValidException("InValidException: %s is invalid. Exception throw: %s" % (check_func.__name__, str(e)), invalid_status)
            return wrapper(self, *args, **kwd)
        return wrapper
    return deco

