import json
import requests
from common.method import Method
from common.sql import Db
def request_ticket():
    url = "http://smartesb-sit2.bankbkemobile.co.id:80/corebank"
    headers = {"Content-Type": "application/json",
               "Connection": "keep-alive"}
    base_url = Method.get_url()
    seq = Method.getLastTime() + Method.generate_random_str(4)
    date = Method.getLastDate()
    timestamp = Method.getTimestamp()

    data = {
        "APP_HEAD":
            {"PAGE_END": "0",
               "CURRENT_NUM": "0",
               "PGUP_OR_PGDN": "0",
               "PAGE_START": "0",
               "TOTAL_NUM": "-1"
            },
        "BODY": {
            "REFERENCE": "ENS20210501701"
        },
        "LOCAL_HEAD": {

        },
        "SYS_HEAD": {
            "MODULE_ID": "CL",
            "TRAN_TIMESTAMP": timestamp,
            "SOURCE_BRANCH_NO": "TEL.507B9D95EC62.zpk",
            "BRANCH_ID": "999",
            "USER_LANG": "CHINESE",
            "SEQ_NO": seq,
            "SOURCE_TYPE": "MT",
            "CORE_SEQ_NO": "",
            "TRAN_CODE": "",
            "PROGRAM_ID": "3221",
            "SERVER_ID": "127.0.0.1",
            "MESSAGE_CODE": "790000",
            "MESSAGE_TYPE": "1300",
            "SERVICE_CODE": "MbsdCore",
            "AUTH_PASSWORD": "",
            "COMPANY": "",
            "APPR_FLAG": "",
            "USER_ID": "linhui",
            "AUTH_FLAG": "N",
            "SCENE_ID": "01",
            "TRAN_TYPE": "",
            "DEST_BRANCH_NO": "999",
            "APPR_USER_ID": "",
            "TRAN_DATE": 20210130,
            "AUTH_USER_ID": "",
            "ORG_SYS_ID": "",
            "TRAN_MODE": "ONLINE",
            "WS_ID": "05",
            "REVERSAL_TRAN_TYPE": ""
        }
    }
    response = requests.post(url= base_url, data=json.dumps(data), headers=headers)
    print(response.json())
request_ticket()