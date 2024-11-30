import json
import requests

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJkZXZAYWlyc3dpZnQuaW8iLCJyZWFsX25hbWUiOiJkZXYiLCJtZXJjaGFudF9pZCI6Im51bGwiLCJ0aW1lX3pvbmUiOm51bGwsImNsaWVudF9pZCI6ImNsaWVudF93ZWIiLCJhdWQiOlsiY2xpZW50X3Jlc291cmNlIl0sInBob25lIjoiIiwicGFyZW50X2lkIjoibnVsbCIsInNjb3BlIjpbImFsbCJdLCJpZCI6IjEwMDQ1IiwiZXhwIjoxNzMyMzA2MDQ2LCJqdGkiOiI1NDkyMDUzMy02OTk2LTQ0ODktYjU4OC1lMDIwYTFiNDU4OWUiLCJlbWFpbCI6ImRldkBhaXJzd2lmdC5pbyJ9.373MpMlBwEzH4Ydci5QFjd7_k2SOd20-yXDH__XxFVo'


def query_order_data(show_result=False):
    url = "https://admin.airswift.io/bw-admin/trade/order/page-query"
    payload = {
        "pageIndex": 0,
        "pageSize": 1000,
        "queryList": [
            {
                "key": "merchantId",
                "value": "100243",
                "oper": ":",
                "join": "andNew"
            }
        ],
        "sortFields": "createTime_d"
    }
    return query(url, payload, show_result)


def query_refund_data(show_result=False):
    url = "https://admin.airswift.io/bw-admin/withdraw/refund/page-query"
    payload = {
        "pageIndex": 1,
        "pageSize": 1000,
        "queryList": [
            {
                "join": "andNew",
                "key": "name",
                "oper": ":",
                "value": "Viiva LLC"
            },
            {
                "key": "status",
                "oper": "!=",
                "value": "0"
            }
        ],
        "sortFields": "createTime_d"
    }
    return query(url, payload, show_result)


def query_withdraw_data(show_result=False):
    url = "https://admin.airswift.io/bw-admin/withdraw/page-query"
    payload = {
        "pageIndex": 1,
        "pageSize": 1000,
        "queryList": [
            {
                "join": "or",
                "key": "relationId",
                "oper": ":",
                "value": "100243"
            },
            {
                "join": "or",
                "key": "name",
                "oper": ":",
                "value": "100243"
            },
            {
                "key": "status",
                "oper": "!=",
                "value": "0"
            }
        ],
        "sortFields": "createTime_d"
    }

    return query(url, payload, show_result)


def query(url, payload, show_result):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Request successful.")
        result_data = response.json()
        if show_result:
            print("Data Retrieved:", json.dumps(result_data, indent=4))
        return result_data
    else:
        print("Failed to retrieve data:", response.status_code)
        print("Details:", response.text)
        return None


# query_order_data(True)
# query_refund_data(True)
# query_withdraw_data(True)
