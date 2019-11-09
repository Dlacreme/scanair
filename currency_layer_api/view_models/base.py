
class BaseViewModel():
    def __init__(self, http_response_data):
        self.success = http_response_data['success']
        self.terms = http_response_data['terms']
        self.privacy = http_response_data['privacy']
