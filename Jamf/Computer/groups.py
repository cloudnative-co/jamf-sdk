from ..client import Client


class ComputerGroups(Client):
    """
    @namespace  Jamf.Computer
    @class      ComputerGroups
    @brief      コンピューターグループ操作用クラス
    """
    path = "computergroups"

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
            super(Groups, self).__init__(company)

    def get(self, id: int = None, name: str = None):
        """
        @brief          コンピューターグループ情報の取得
        @details        idもしくはnameの指定がある場合は指定内容を返却します
        @n              無指定の場合、一覧情報を返します
        @params[in]     id      コンピューターグループのIDを指定
        @params[in]     name    コンピューターグループの名前を指定
        @return         dict     取得した情報を返却します
        """
        path = self.create_path(self.path, id, name)
        response = self.request(method="get", path=path, to_dict=True)
        return response

    def post(self, payload: dict):
        """
        @brief          コンピューターグループ情報の登録
        @params[in]     登録する内容を辞書データにて指定
        @return         dict     登録したコンピューターグループのIDを返却します
        """
        response = self.request(
            method="post",
            path=self.path,
            payload=payload,
            to_dict=True,
            to_xml=True
        )
        return response

    def put(self, payload: dict, id: int = None, name: str = None):
        """
        @brief          コンピューターグループ情報の更新
        @details        idもしくはnameにて指定されたコンピューターグループを
        @n              payloadの内容にて更新します
        @params[in]     id      コンピューターグループのIDを指定
        @params[in]     name    コンピューターグループの名前を指定
        @return         dict    更新したコンピューターグループのIDを返却します
        """
        path = self.create_path(self.path, id, name)
        response = self.request(
            method="put",
            path=path,
            payload=payload,
            to_dict=True,
            to_xml=True
        )
        return response

    def delete(self, id: int = None, name: str = None):
        """
        @brief          コンピューターグループ情報の削除
        @details        idもしくはnameにて指定されたコンピューターグループを
        @n              削除します
        @params[in]     id      コンピューターグループのIDを指定
        @params[in]     name    コンピューターグループの名前を指定
        @return         dict    削除したコンピューターグループのIDを返却します
        """
        path = self.create_path(self.path, id, name)
        response = self.request(method="delete", path=path, to_dict=True)
        return response
