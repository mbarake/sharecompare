import streamlit as st
from compare import Compare
from constants import PARAM, TAXI, RENT, SHARE
import pandas as pd
import matplotlib.pyplot as plt

class UI:


    
    @staticmethod
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i], y[i], ha = 'center')

    def __init__(self) -> None:
        self.sim = Compare()

    def create_ui(self):
        st.header('Comparison of costs between owning and sharing a car.')
        st.markdown('#')
        with st.sidebar:
            # Creating sliders for parameters
            st.title("General Param")
            period = st.slider('Period in years', min_value=1, max_value=20, value=PARAM.PERIOD)
            kmdriven = st.slider('KM Driver per year', min_value=100, max_value=25000, value=PARAM.KMDRIVERPERYEAR)
           
            st.divider()

            st.title("Car Ownership")
           
            costperyear = st.slider('Price of the car per year', min_value=500, max_value=5000, value=PARAM.COSTPERYEAR, step=10)
            fuelprice = st.slider('Fuel price per liter', min_value=1.0, max_value=2.0, value=PARAM.FUELPRICE, step=0.01)
            insurance = st.slider('Insurance cost per year', min_value=500, max_value=5000, value=PARAM.INSURANCE)
            roadtax = st.slider('Road Tax per year', min_value=0, max_value=1000, value=PARAM.ROADTAX, step =10)
            maintenance = st.slider('AVG Maintenance cost per year', min_value=250, max_value=2000, value=PARAM.MAINENANCE)
            efficiency = st.slider('Fuel Economy in liter/100km', min_value=3, max_value=20, value=PARAM.EFFICIENCY)
            st.write ('UK MPG:', round((100 * 4.54609)/(1.609344*efficiency),2)) 
            st.write ('US MPG:', round((100 * 3.785411784)/(1.609344*efficiency),2)) 
            
          
            st.divider()
            st.title("Car Sharing")
            share_rate = st.slider('Daily rate', min_value=45, max_value=150, value=SHARE.RATE)
            share_km_rate = st.slider('Rate per km', min_value=0.2, max_value=0.25, value=SHARE.KMRATE, step=0.01)
            share_freq = st.slider('How many days shared per month', min_value=1, max_value=30, value=SHARE.HOWMANYTIMESPERMONTH)
            share_travel = st.slider('Cost of travelling forth and back to get the car', min_value=0, max_value=30, value=SHARE.TRAVEL)

            st.divider()
            st.title("Car Rental")
            rent_rate = st.slider('Daily rate', min_value=20, max_value=150, value=RENT.RATE)
            rent_freq = st.slider('How many days rented per month', min_value=1, max_value=30, value=RENT.HOWMANYTIMESPERMONTH)
            rent_travel = st.slider('Cost of travelling forth and back to get the car', min_value=0, max_value=30, value=RENT.TRAVEL)

            st.divider()
            st.title("Hire a Taxi")
            taxi_rate = st.slider('Cost per KM', min_value=1, max_value=10, value=TAXI.RATE)
           
       
       
        self.sim.period = period
        self.sim.km_driver_per_year = kmdriven
        self.sim.cost_per_year = costperyear
        self.sim.fuel_price = fuelprice
        self.sim.insurance = insurance
        self.sim.roadtax = roadtax
        self.sim.maintenance = maintenance
        self.sim.efficiency = efficiency
        
        self.sim.share_freq = share_freq
        self.sim.share_travel = share_travel
        self.sim.share_rate = share_rate
        self.sim.share_km_rate = share_km_rate

        self.sim.rent_freq = rent_freq
        self.sim.rent_price = rent_rate
        self.sim.rent_travel = rent_travel
        
        self.sim.taxi_rate = taxi_rate

      
        res = self.sim.get_results()

        data = {
            "Commute Type": ["Car Ownership", "Car Share", "Car Rental", "Taxi Hire"],
            "Cost": res  # Example prices in dollars
        }

        df = pd.DataFrame(data)

     
        fig, ax = plt.subplots()
        ax.bar(df["Commute Type"], df["Cost"], color=['blue', 'green', 'red'])
        ax.set_xlabel("Category")
        ax.set_ylabel("Cost")
        ax.set_title(f"""Total price of Different Commute Types over {PARAM.PERIOD} years""")
        self.addlabels(df["Commute Type"],  df["Cost"])


        st.pyplot(fig)
        st.markdown('#')
        st.text("Car Share has a typical rate between 50 and 80 euros per day and 50 km free per day. \n If you exceed 50 km you are charged at around €0.25 per km.")
        
        multi = '''This is closely based on some of the car types found at Yuko, GOCAR and Driveyou. 
                   For different options and locations visit their sites for accurate pricing and details.
                '''
        st.markdown('#')
        st.markdown(multi)

        st.write("By Mousbah Barake (https://www.linkedin.com/in/mbarake/)")
       

        st.markdown(
            '<div style="margin-top: 0.75em;"><a href="https://www.honeyincoffee.com/" target="_blank"><img src="https://primary.jwwb.nl/public/p/n/q/temp-kpsnnbdlqeuhnoqwnbla/3alqt3/man2oushe_honey_in_coffee_87904c0b-741f-4f4d-9ef0-22e5387bf01a.png?enable-io=true&enable=upscale&crop=864%2C864%2Cx0%2Cy0%2Csafe&width=98&height=98" alt="Buy Me A Coffee" height="100" width="100"></a></div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div style="margin-top: 0.75em;"><a href="https://www.buymeacoffee.com/mbarake" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a></div>',
            unsafe_allow_html=True,
        )
       

if __name__ == "__main__":
    ui = UI()
    ui.create_ui()