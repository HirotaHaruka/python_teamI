import mst_merchandise_edit
import tbl_stock_edit
import tbl_money_edit
import tbl_message_edit

def edit_stock(id_stock_dic):
    for key,value in id_stock_dic.items():
        tbl_stock_edit.Tbl_Money_update(key, value)

def edit_money(price_cnt_dic):
    for key,value in price_cnt_dic.items():
        tbl_money_edit.Tbl_Money_update(key, value)

def main(id_stock_dic, price_cnt_dic):
    edit_stock(id_stock_dic)
    edit_money(price_cnt_dic)

