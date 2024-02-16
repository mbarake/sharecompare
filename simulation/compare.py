from constants import PARAM, RENT, SHARE, TAXI

class Compare:


    def __init__(self) -> None:
        self.share_km_rate = SHARE.KMRATE
        self.share_rate = SHARE.RATE
        self.share_freq = SHARE.HOWMANYTIMESPERMONTH
        self.share_travel = SHARE.TRAVEL
        self.share_free = SHARE.FREE

        self.rent_price = RENT.RATE
        self.rent_travel = RENT.TRAVEL
        self.rent_freq = RENT.HOWMANYTIMESPERMONTH

        self.period = PARAM.PERIOD
        self.km_driver_per_year = PARAM.KMDRIVERPERYEAR
        self.cost_per_year = PARAM.COSTPERYEAR
        self.efficiency = PARAM.EFFICIENCY
        self.insurance = PARAM.INSURANCE
        self.roadtax = PARAM.ROADTAX
        self.maintenance =  PARAM.MAINENANCE
        self.fuel_price = PARAM.FUELPRICE
        
        self.taxi_rate = TAXI.RATE

    def calc_car(self):
        cost_car = self.cost_per_year*self.period
        fuel = self.period*self.km_driver_per_year*(self.efficiency/100)*self.fuel_price
        cost = self.period*(self.insurance+self.roadtax+self.maintenance) 
        return cost_car+fuel+cost
    
    def calc_share(self):
        km_driven = self.period*self.km_driver_per_year - self.share_freq*12*self.period*self.share_free
        fuel_price = float(km_driven)*self.share_km_rate if km_driven >0 else 0
        rent_price = self.share_freq*12*self.period*self.share_rate
        travel = self.share_travel*self.share_freq*12*self.period
        return fuel_price+rent_price+travel

    
    def calc_rental(self):
        travel = self.rent_travel*self.rent_freq*12*self.period
        fuel = self.period*self.km_driver_per_year*(self.efficiency/100)*self.fuel_price
        cost =  self.rent_freq*12*self.period*self.rent_price
        return travel+fuel+cost

    
    def calc_taxi(self):
        cost = self.taxi_rate*self.km_driver_per_year*self.period
        return cost

    def get_results(self):
        costcar = self.calc_car()
        costshare = self.calc_share()
        costrental = self.calc_rental()
        costtaxi = self.calc_taxi()
        return [costcar, costshare, costrental, costtaxi]


if __name__=="__main__": 
    cmp = Compare()
    print(cmp.get_results())





