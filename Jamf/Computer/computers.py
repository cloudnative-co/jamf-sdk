from ..client import Client


class Computers(Client):
    """
    @namespace  Jamf.Computer
    @class      Computers
    @brief      コンピューター操作用クラス
    """
    path = "computers"

    def __init__(self, company: str = None, client: Client = None):
        """
        @brief          初期化
        @params[in]     company ドメインに指定する会社名
        @params[in]     client  Clientを継承したクラスのオブジェクトを指定
        @details        companyもしくはclientを指定して
        @n              クラスオブジェクトを初期化します
        """
        if client is not None:
            self.session = client.session
            self.host = client.host
            self.headers = client.headers
        elif company is not None:
            super(Computers, self).__init__(company)

    def get(self, id: int = None, name: str = None):
        """
        @brief          コンピューター情報の取得
        @details        idの指定がある場合は指定内容を返却します
        @n              無指定の場合、一覧情報を返します
        @params[in]     id      コンピューターのIDを指定
        @return         dict    取得した情報を返却します
        """
        path = self.create_path(self.path, id, name)
        response = self.request(method="get", path=path, to_dict=True)
        return response

