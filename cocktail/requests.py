import aiohttp 
from aiohttp import client_exceptions as errs

class Reqs:
    """Methods to handle requests"""

    @classmethod ## creating one instance for all requests
    def ses(self):
        self.ses = aiohttp.ClientSession()
        return self.ses

    @staticmethod ## check for headers
    def header_check(headers: any = None):
        if not headers:
            headers = {}
        else:
            headers = {headers}

        return headers

    @staticmethod ## check for data {PUT & POST} 
    def data_check(data: any = None):
        if not data:
            data = {}
        else:
            data = {data}

        return data

    @classmethod ## GET request
    async def get(self, url: str, *, headers: any = None):
        headers = Reqs.header_check(headers)
        ses = Reqs.ses()
        async with ses.get(url, headers=headers) as r:
            try:
                if r.status in range(200, 299):
                    data = await r.json()
                    return data
                else:
                    print('Endpoint Response: '+r.status)
            except errs.ContentTypeError:
                if r.status in range(200, 299):
                    data = await r.json(content_type="text/html")
                    return data
                else:
                    print('Endpoint Response: '+r.status)
        
        @classmethod ## POST request
        async def post(self, url: str, *, headers: any = None, data: any = None):
            headers = Reqs.header_check(headers)
            data = Reqs.data_check(data)
            ses = Reqs.ses()
            async with ses.post(url, headers=headers, data=data) as r:
                try:
                    if r.status in range(200, 299):
                        data = await r.json()
                        return data
                    else:
                        print('Endpoint Response: '+r.status)
                except errs.ContentTypeError:
                    if r.status in range(200, 299):
                        data = await r.json(content_type="text/html")
                        return data
                    else:
                        print('Endpoint Response: '+r.status)


