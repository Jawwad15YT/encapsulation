class Kings_Computers():
    def __init__(self,purchase_price,selling_price,product_name):
        self.__purchase_price = purchase_price
        self.selling_price = selling_price
        self.product_name = product_name

    def GetPurchasePrice(self):
        print(self.__purchase_price)

primaryproduct = Kings_Computers(154960,174960,"FrostBite_Prebuilt")
secondary = Kings_Computers(120000,140000,"The_Kudan_Level_10")

primaryproduct.GetPurchasePrice()
