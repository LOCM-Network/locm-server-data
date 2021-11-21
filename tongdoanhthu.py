from datetime import date
from requests import get

def cc_fee(card_type, amount):
	fees = get("https://thesieure.com/chargingws/v2/getfee?partner_id=2272505261")
	data = fees.json()
	for card in data:
		if card["telco"] == card_type.upper() and card["value"] == amount:
			fee = card["fees"]
			dt_fee = (amount * fee) / 100
			return amount - dt_fee

sv = "prison" # tính sv nào để sv đó!

doanhthu_card = 0
doanhthu_r = 0
data_cards = {"Viettel" : 0, "Vinaphone" : 0, "Mobifone": 0}

with open('doanhthu11.txt', 'r') as f:
	datalist = f.readlines()

for data in datalist:
	if sv == "skyblock":
		amount = int(data.split("|")[1])
		card_type = data.split("|")[3].replace("\n", "")
	if sv == "prison":
		amount = int(data.split(" | ")[1].replace("AMOUNT: ", ""))
		card_type = data.split(" | ")[0].replace("CARD: ", "")
		
	doanhthu_card += amount
	if card_type in data_cards:
		data_cards[card_type] += amount
		doanhthu_r += cc_fee(card_type, amount)

today = date.today().strftime("%d/%m/%Y")
print("Doanh thu (" + sv + ") tháng 11 tính đến ngày (" + today + "): " + str(doanhthu_card) + " VND (CARD)")
print("Tổng doanh thu sau phí: " + str(doanhthu_r) + "VND")
for data in data_cards:
	print(data + ": " + str(data_cards[data]) + " VND")
