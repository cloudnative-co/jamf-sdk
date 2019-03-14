# Jamf-SDK for Python  
Jamfへのアクセス用ライブラリ

## 前提
PythonとJamfに対して最低限度の用法が理解できている人を対象とします。

## 依存
 - python 3.6
 - requestsライブラリ
 - xmltodictライブラリ

## Install
pythonのpipにてinstall元にgitを指定することで自動的にpython用のライブラリとしてインストールされます

`pip install git+ssh://git@github.com/cloudnative-co/jamf-sdk.git`

## 用法

### Clientインスタンスの作成

#### 引数
| 引数 | 説明 |
| --- | --- |
|company | 使用するドメイン名を指定。 https://[ compnay ].jamfcloud.com/  |

#### example
```
import json
import Jamf
jamf_client = Jamf.Client(company="foo")
jamf_client.login(username, password)
jamf_computers = Jamf.Computer.Computers(client=jamf_client)
response = jamf_computers.get()
print(json.dumps(response, indent=4))
```

