import json
import csv

tx_json = '../data/temp.json'
# tx_csv = '../data/temp.csv'

total: float = 0.0

with open(tx_json, 'r') as f:
    data = json.load(f)

for i in data['data']['records']:
    total += i['amount']

print('Total Amount:', total)
print('After withdraw deduction:', total - (844.038 + 1048.35))

# with open(tx_csv, mode='w', newline='') as csv_file:
#     fieldnames = ['application_name', 'currency', 'order_amount', 'merchant_fee', 'pay_amount', 'status', 'create_time', 'pay_time', 'transaction_id']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # writer.writeheader()

    # for i in data['data']['records']:
        # order_counter += 1
        # if i['txId'] is not None:
        #     order_amount = float(i['amount'])
        #
        #     total_tx_amount += order_amount
        #     total_tx_fee += order_amount * 0.025
        #     total_revenue += order_amount * 0.975
        #
        #     writer.writerow({
        #         'application_name': i.get('appName', None),
        #         'currency': i.get('coinUnit', None),
        #         'order_amount': order_amount,
        #         'merchant_fee': order_amount * 0.025,  # 2.5% transaction fee
        #         'pay_amount': order_amount * 0.975,  # 97.5% revenue
        #         'status': pay_status.get(i.get('payStatus')),
        #         'create_time': i.get('createTimeStr', None),
        #         'pay_time': i.get('payTimeStr', None),
        #         'transaction_id': i.get('txId', None)
        #     })

# print('Total Number of Transactions:', order_counter)
# print('Total Transaction Amount:', total_tx_amount)
# print('Total Transaction Fee:', total_tx_fee)
# print('Total Merchant Revenue:', total_revenue)
