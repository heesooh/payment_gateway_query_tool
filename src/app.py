import csv
from query import query_order_data, query_refund_data, query_withdraw_data


def order_data_to_csv():
    data = query_order_data()

    if data:
        file_name = '../data/order.csv'

        total_order_revenue: float = 0
        total_order_amount: float = 0
        total_order_fee: float = 0
        order_counter: int = 0

        pay_status = {
            0: "PENDING",
            1: "SUCCESS",
            2: "CANCELLED",
            3: "UNDERPAID",
            4: "OVERPAID"
        }

        with open(file_name, mode='w', newline='') as csv_file:
            fieldnames = ['application_name', 'currency', 'order_amount', 'merchant_fee', 'merchant_revenue',
                          'pay_amount', 'status', 'create_time', 'pay_time', 'transaction_id']

            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for i in data['data']['records']:
                # order_counter += 1 if i.get('payStatus') != 2 else 0
                if i['txId'] is not None:
                    order_counter += 1
                    order_amount = float(i['amount'])

                    total_order_amount += order_amount
                    total_order_fee += order_amount * 0.025
                    total_order_revenue += order_amount * 0.975

                    writer.writerow({
                        'application_name': i.get('appName', None),
                        'currency': i.get('coinUnit', None),
                        'order_amount': order_amount,
                        'merchant_fee': order_amount * 0.025,  # 2.5% transaction fee
                        'merchant_revenue': order_amount * 0.975,  # 97.5% revenue
                        'pay_amount': i.get('payAmount', None),
                        'status': pay_status.get(i.get('payStatus')),
                        'create_time': i.get('createTimeStr', None),
                        'pay_time': i.get('payTimeStr', None),
                        'transaction_id': i.get('txId', None)
                    })

        print('Total Number of Successful/Overpaid Orders:', order_counter)
        print('Total Order Amount:', total_order_amount)
        print('Total Order Fee:', total_order_fee)
        print('Total Merchant Revenue:', total_order_revenue)
    else:
        print("Retrieved empty data")


def refund_data_to_csv():
    response = query_refund_data()

    if response:
        file_name = '../data/refund.csv'

        total_refund_amount: float = 0
        total_refund_fee: float = 0
        refund_counter: int = 0

        with open(file_name, mode='w', newline='') as csv_file:
            fieldnames = ['refund_id', 'currency', 'refund_amount', 'refund_fee',
                          'create_time', 'audit_time', 'refund_address', 'hash_id']

            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for i in response['data']['records']:
                # order_counter += 1 if i.get('payStatus') != 2 else 0
                if i['txId'] is not None:
                    refund_counter += 1
                    order_amount = float(i['amount'])

                    total_refund_amount += order_amount
                    total_refund_fee += 3

                    writer.writerow({
                        'refund_id': i.get('id'),
                        'currency': i.get('digitalCoinUnit'),
                        'refund_amount': order_amount,
                        'refund_fee': 3,
                        'create_time': i.get('createTimeStr'),
                        'audit_time': i.get('auditTimeStr'),
                        'refund_address': i.get('address'),
                        'hash_id': i.get('txId'),
                    })

        print('Total Number of Successful Refund:', refund_counter)
        print('Total Refund Amount:', total_refund_amount)
        print('Total Refund Fee:', total_refund_fee)
    else:
        print("Retrieved empty data")


def withdraw_data_to_csv():
    response = query_withdraw_data()

    if response:
        file_name = '../data/withdraw.csv'

        total_withdraw_amount: float = 0
        total_withdraw_fee: float = 0
        withdraw_counter: int = 0

        with open(file_name, mode='w', newline='') as csv_file:
            fieldnames = ['withdraw_id', 'currency', 'withdraw_amount', 'withdraw_fee',
                          'create_time', 'audit_time', 'withdraw_address', 'hash_id']

            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for i in response['data']['records']:
                # order_counter += 1 if i.get('payStatus') != 2 else 0
                if i['txId'] is not None:
                    withdraw_counter += 1
                    order_amount = float(i['amount'])

                    total_withdraw_amount += order_amount
                    total_withdraw_fee += 3

                    writer.writerow({
                        'withdraw_id': i.get('id'),
                        'currency': i.get('digitalCoinUnit'),
                        'withdraw_amount': order_amount,
                        'withdraw_fee': 3,
                        'create_time': i.get('createTimeStr'),
                        'audit_time': i.get('auditTimeStr'),
                        'withdraw_address': i.get('address'),
                        'hash_id': i.get('txId'),
                    })

        print('Total Number of Successful Withdraw:', withdraw_counter)
        print('Total Withdraw Amount:', total_withdraw_amount)
        print('Total Withdraw Fee:', total_withdraw_fee)
    else:
        print("Retrieved empty data")


order_data_to_csv()
refund_data_to_csv()
withdraw_data_to_csv()