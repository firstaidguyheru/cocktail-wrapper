import aiohttp 
from aiohttp import client_exceptions as errs

class BadResponse(Exception):
    def __init__(self, message):
        super(BadResponse, self).__init__(message)

class Reqs:
    ses = aiohttp.ClientSession()
    """Methods to handle requests"""

    def __init__(self):
        self.ses = aiohttp.ClientSession()

    @staticmethod ## check for headers
    def header_check(headers: any = None):
        if not headers:
            headers = {}
        else:
            headers = {headers}

        return headers

    @staticmethod ## check for data {POST} 
    def data_check(data: any = None):
        if not data:
            data = {}
        else:
            data = {data}

        return data

    @classmethod ## GET request
    async def get(self, url: str, *, headers: any = None):
        headers = Reqs.header_check(headers)
        ses = self.ses
        async with ses.get(url, headers=headers) as r:
            try:
                if r.status in range(200, 299):
                    data = await r.json()
                    return data
                else:
                    raise BadResponse(r.status)
            except errs.ContentTypeError:
                if r.status in range(200, 299):
                    data = await r.json(content_type="text/html")
                    return data
                else:
                    raise BadResponse(r.status)
    
    @classmethod ## POST request
    async def post(self, url: str, *, headers: any = None, data: any = None):
        headers = Reqs.header_check(headers)
        data = Reqs.data_check(data)
        ses = self.ses
        async with ses.post(url, headers=headers, data=data) as r:
            try:
                if r.status in range(200, 299):
                    data = await r.json()
                    return data
                else:
                    raise BadResponse(r.status)
            except errs.ContentTypeError:
                if r.status in range(200, 299):
                    data = await r.json(content_type="text/html")
                    return data
                else:
                    raise BadResponse(r.status)