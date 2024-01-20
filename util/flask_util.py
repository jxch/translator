def param(field, request):
    if request.method == "GET":
        return request.args.get(field)
    elif request.method == "POST":
        return request.json.get(field)
    raise Exception("不支持这种请求方法")


def param_list(field, request):
    if request.method == "GET":
        return request.args.getlist(field)
    elif request.method == "POST":
        return request.json.get(field)
    raise Exception("不支持这种请求方法")