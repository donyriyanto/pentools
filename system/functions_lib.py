from flask import Response
import json

def response(data=None,code=200,message='Success'):
    res = {"data":data,'meta': {'message': message, 'code': code}}
    res = json.dumps(res)
    resp = Response(res, status=code, mimetype='application/json')
    return resp