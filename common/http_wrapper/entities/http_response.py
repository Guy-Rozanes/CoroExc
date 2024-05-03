from json import JSONDecodeError


class HttpResponse:

    def __init__(self, response):
        self.status_code = response.status_code
        if response.text != '':
            try:
                self.content = response.json()
            except JSONDecodeError:
                self.content = response.text
        else:
            self.content = {}
