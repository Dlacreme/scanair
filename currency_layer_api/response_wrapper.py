class ResponseWrapper():

    def __init__(self, status, url, method, params, result):
        # HTTP Code result
        self.status = status
        # Url fetched
        self.url = url
        # Http Method used
        self.method = method
        # Params sent
        self.params = params
        # Result data
        self.result = result

    def is_failure(self):
        return self.status >= 300