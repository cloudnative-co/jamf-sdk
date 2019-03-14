import base64
import requests
import xmltodict


class Client(object):
    session = None
    headers: dict = dict()
    host: str = None

    def __init__(self, company: str):
        self.session = requests.Session()
        self.host = "https://{}.jamfcloud.com/".format(company)

    def login(self, user: str, password: str):
        auth = "{}:{}".format(user, password)
        auth = auth.encode('utf8')
        auth = base64.b64encode(auth)
        auth = auth.decode()
        auth = "Basic {}".format(auth)
        print(auth)
        ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
            + "AppleWebKit/537.36 (KHTML, like Gecko) " \
            + "Chrome/70.0.3538.77 Safari/537.36'
        self.headers = {
            'User-Agent': ua,
            "Authorization": auth,
        }

    def request(
        self,
        method: str, path: str,
        query: dict = None, payload: dict = None,
        to_dict: bool = False, to_xml: bool = False
    ):
        method = method.lower()
        url = "{}JSSResource/{}".format(self.host, path)
        args = {
            "url": url,
            "headers": self.headers
        }
        if query is not None:
            args["params"] = query
        if payload is not None:
            if to_xml:
                payload = xmltodict.unparse(payload)
                args["headers"]["Content-Type"] = "application/xml"
            args["data"] = payload

        response = getattr(self.session, method)(**args)
        if response.status_code in [200, 201, 204]:
            if to_dict:
                data = response.text
                return xmltodict.parse(data)
            else:
                return response.text
        else:
            response.raise_for_status()

    def create_path(self, base:str, id: int = None, name: str = None):
        if id is not None:
            path = "{}/id/{}".format(base, id)
        elif name is not None:
            path = "{}/name/{}".format(base, name)
        else:
            path = base
        return path
