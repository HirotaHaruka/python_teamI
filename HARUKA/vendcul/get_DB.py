import mst_merchandise_edit
import tbl_stock_edit
import tbl_money_edit
import tbl_message_edit

def get_id_name():
    name_id = {}
    mst_tbl = mst_merchandise_edit.Mst_Merchandise_select()
    for i in mst_tbl:
        name_id[i.name] = i.id
    return name_id

def get_id_price():
    id_price = {}
    mst_tbl = mst_merchandise_edit.Mst_Merchandise_select()
    for i in mst_tbl:
        id_price[i.id] = i.price
    return id_price
    
def get_money_tbl():
    price_cnt = {}
    for i in [5000,1000,500,100,50,10]:
        price_cnt[i] = tbl_money_edit.tbl_select(i)[0][0]
    return price_cnt

def get_stock():
    id_stock_cnt = {}
    tbl_stock = tbl_stock_edit.tbl_select()
    for i in tbl_stock:
        id_stock_cnt[int(i.id)] = int(i.stock)
    return id_stock_cnt

def main():
    name_id = get_id_name()
    id_price = get_id_price()
    price_cnt = get_money_tbl()
    id_stock_cnt = get_stock()
    return name_id, id_price, price_cnt, id_stock_cnt