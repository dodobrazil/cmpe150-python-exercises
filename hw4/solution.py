input_file = "input.txt"  

with open(input_file, "r", encoding="utf-8") as file:
    orders = [line.strip() for line in file.readlines()]

parsed_orders = []
for order in orders:
    parts = order.split()
    parsed_orders.append({
        "timestamp": parts[0],  #YYYY-MM-DD-hh-mm-ss
        "user_id": int(parts[1]),
        "username": parts[2],
        "stock": parts[3],
        "order_type": parts[4],
        "shares": int(parts[5]),
        "price": float(parts[6])
    })

def sort_key(order):
    return (
        order["timestamp"],
        order["stock"],
        order["price"] if order["order_type"] == "Sell" else -order["price"],
        order["user_id"]
    )

# Tüm emirleri kopyala, sıfırdan sıralamaca ve eşleştirmece
all_orders = [o.copy() for o in parsed_orders]
all_orders.sort(key=sort_key)

buy_orders = []
sell_orders = []
matched_orders = []
#buy veya sell order olmasına göre gruplamaca
for order in all_orders:
    if order["order_type"] == "Buy":
        buy_orders.append(order)
    elif order["order_type"] == "Sell":
        sell_orders.append(order)
#genel eşleşme kuralları
for buy in buy_orders[:]:
    for sell in sell_orders[:]: 
        if (buy["stock"] == sell["stock"] and 
            buy["price"] >= sell["price"] and 
            buy["user_id"] != sell["user_id"]):

            matched_shares = min(buy["shares"], sell["shares"])
            if matched_shares == 0:
                continue

            full_timestamp = max(buy["timestamp"], sell["timestamp"])

            matched_orders.append({
                "buyer": buy["username"],
                "seller": sell["username"],
                "stock": buy["stock"],
                "shares": matched_shares,
                "price": sell["price"],
                "timestamp": full_timestamp
            })

            buy["shares"] -= matched_shares
            sell["shares"] -= matched_shares

            if buy["shares"] == 0 and buy in buy_orders:
                buy_orders.remove(buy)
            if sell["shares"] == 0 and sell in sell_orders:
                sell_orders.remove(sell)

# Lambda yasak olduğu için(hocam lütfen öğretin kullanalım artık :d) manuel lambda yazıyoruz
def match_sort_key(order):
    return order["timestamp"]

matched_orders.sort(key = match_sort_key)

def total_executed_volume(input_time):#toplam yapılan işlem hacmii
    input_time = input_time.replace(" ", "-").replace(":", "-")
    total_volume = 0
    for match in matched_orders:
        match_time = match['timestamp']
        if match_time <= input_time:
            total_volume += match['shares'] * match['price']
    return int(total_volume)

def executed_user_volume(user_id, input_time):#kişiye özel uygulanan işlem hacmi
    input_time = input_time.replace(" ", "-").replace(":", "-")
    user_volume = 0

    for match in matched_orders:
        buyer_id = None
        seller_id = None
        for order in all_orders:
            if order["username"] == match["buyer"]:
                buyer_id = order["user_id"]
            if order["username"] == match["seller"]:
                seller_id = order["user_id"]

        match_time = match['timestamp']
        if match_time <= input_time and (user_id == buyer_id or user_id ==seller_id):
            user_volume += match['shares'] * match['price']

    return int(user_volume)



def total_remaining_volume(input_time): #kalan hacim bulma
    input_time = input_time.replace(" ", "-").replace(":", "-")

    filtered_orders = [o for o in parsed_orders if o["timestamp"] <= input_time]
    filtered_orders = [o.copy() for o in filtered_orders]
    filtered_orders.sort(key=sort_key)

    temp_buy = []
    temp_sell = []
    for order in filtered_orders:
        if order["order_type"] == "Buy":
            temp_buy.append(order)
        else:
            temp_sell.append(order)

    for b in temp_buy[:]:
        for s in temp_sell[:]:
            if b["stock"] == s["stock"] and b["price"] >= s["price"] and b["user_id"] != s["user_id"]:
                matched_shares = min(b["shares"], s["shares"])
                if matched_shares == 0:
                    continue
                b["shares"] -= matched_shares
                s["shares"] -= matched_shares

                if b["shares"] == 0 and b in temp_buy:
                    temp_buy.remove(b)
                if s["shares"] == 0 and s in temp_sell:
                    temp_sell.remove(s)

    total_volume =  0
    for o in temp_buy + temp_sell:
        if o["shares"] > 0:
            total_volume += o["shares"] * o["price"]

    return int(total_volume)



def remaining_user_volume(user_id, input_time): #kişi kullanılamayn hacim bulma
    input_time = input_time.replace(" ", "-").replace(":", "-")

    filtered_orders = [o for o in parsed_orders if o["timestamp"] <= input_time]
    filtered_orders = [o.copy() for o in filtered_orders]
    filtered_orders.sort(key=sort_key)

    temp_buy =  []
    temp_sell = []
    for order in filtered_orders:
        if order["order_type"] == "Buy":
            temp_buy.append(order)
        else:
            temp_sell.append(order)

    for b in temp_buy[:]:
        for s in temp_sell[:]:
            if b["stock"] == s["stock"] and b["price"] >= s["price"] and b["user_id"] != s["user_id"]:
                matched_shares = min(b["shares"], s["shares"])
                if matched_shares == 0:
                    continue
                b["shares"] -=   matched_shares
                s["shares"] -= matched_shares

                if b["shares"] == 0 and b in temp_buy:
                    temp_buy.remove(b)
                if s["shares"] == 0 and s in temp_sell:
                    temp_sell.remove(s)



    total_volume = 0
    for o in temp_buy + temp_sell:
        if o["shares"] > 0 and o["user_id"] == user_id:
            total_volume += o["shares"] * o["price"]

    return int(total_volume)



output_file = "output.txt"
with open(output_file, "w", encoding="utf-8") as file:
    for match in matched_orders:
        date_part = match['timestamp'][:10]  # YYYY-MM-DD
        time_part = match['timestamp'][11:]  # hh-mm-ss
        time_part = time_part.replace('-', ':')  # hh:mm:ss formatına çevirme
        line = (
            f"{match['buyer']} bought {match['shares']} {match['stock']} "
            f"for {match['price']} USD from {match['seller']} on {date_part} at {time_part}\n"
        )
        file.write(line)
        print(line, end="")

#İnput alırken - yazdırırken : kullandığımızı fark edene kadar hayatımdan 2 saat harcadım.
