from constants import YUKOConst, GOConst

class Compare:

    PERIOD = 10
    KMDRIVERPERYEAR= 5000
    HOWMANYTIMESPERMONTH = 2
    FUELPRICE = 1.68
    COSTPERYEAR = 1000
    EFFICIENCY = 7  #l per 100km
    INSURANCE = 2000 # per year
    ROADTAX = 300 
    MAINENACE = 500
    COSTPERYEAR = 1000
    TRAVELTOSHARE = 5
  
    def __init__(self) -> None:
        pass


    def calc_go(self):
        km_driven = Compare.KMDRIVERPERYEAR*Compare.PERIOD - Compare.HOWMANYTIMESPERMONTH*12*Compare.PERIOD*GOConst.FREE
        fuel_price = km_driven*GOConst.RATE
        rent_price = Compare.HOWMANYTIMESPERMONTH*12*Compare.PERIOD*GOConst.PRICE
        travel = Compare.TRAVELTOSHARE*Compare.HOWMANYTIMESPERMONTH*12*Compare.PERIOD
        return fuel_price+rent_price+travel

    def calc_yuko(self):
        km_driven = Compare.KMDRIVERPERYEAR*Compare.PERIOD - Compare.HOWMANYTIMESPERMONTH*12*Compare.PERIOD*YUKOConst.FREE
        fuel_price = km_driven*YUKOConst.RATE
        rent_price = Compare.HOWMANYTIMESPERMONTH*12*Compare.PERIOD*YUKOConst.PRICE
        travel = Compare.TRAVELTOSHARE*Compare.HOWMANYTIMESPERMONTH*12*Compare.PERIOD
        return fuel_price+rent_price+travel

    def calc_car(self):
        cost_car = Compare.COSTPERYEAR*Compare.PERIOD
        fuel = Compare.PERIOD*Compare.KMDRIVERPERYEAR*(Compare.EFFICIENCY/100)*Compare.FUELPRICE
        cost = Compare.PERIOD*(Compare.INSURANCE+Compare.ROADTAX+Compare.MAINENACE) 
        return cost_car+fuel+cost
    

    def get_results(self):
        costcar = self.calc_car()
        costyuk = self.calc_yuko()
        costgo = self.calc_go()
        return [costcar, costyuk, costgo]


if __name__=="__main__": 
    cmp = Compare()
    print(cmp.get_results())





