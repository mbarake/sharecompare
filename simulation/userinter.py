import streamlit as st
from compare import Compare
from constants import PARAM
import pandas as pd
import matplotlib.pyplot as plt

class UI:
    
    @staticmethod
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i], y[i], ha = 'center')
     
    def create_ui(self):
        st.header('Comparison of costs between owning and sharing a car.')
        st.markdown('#')
        with st.sidebar:
            # Creating sliders for parameters
            st.title("General Param")
            period = st.slider('Period in years', min_value=1, max_value=20, value=PARAM.PERIOD)
            kmdriven = st.slider('KM Driver per year', min_value=1000, max_value=25000, value=PARAM.KMDRIVERPERYEAR)
           

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
            howmany = st.slider('How many days rented/shared per month', min_value=1, max_value=30, value=PARAM.HOWMANYTIMESPERMONTH)
            travel = st.slider('Cost of travelling forth and back to get the car', min_value=0, max_value=30, value=PARAM.TRAVELTOSHARE)
           
       
        sim = Compare()
        Compare.PERIOD=period
        Compare.KMDRIVERPERYEAR=kmdriven
        Compare.HOWMANYTIMESPERMONTH=howmany
        Compare.FUELPRICE = fuelprice
        Compare.COSTPERYEAR = costperyear
        Compare.INSURANCE=insurance
        Compare.ROADTAX = roadtax
        Compare.MAINENACE = maintenance
        Compare.EFFICIENCY = efficiency
        Compare.TRAVELTOSHARE = travel

        res = sim.get_results()

        data = {
            "Commute Type": ["Car Ownership", "Car Share 1", "Car Share 2"],
            "Price": res  # Example prices in dollars
        }


        df = pd.DataFrame(data)

     
        fig, ax = plt.subplots()
        ax.bar(df["Commute Type"], df["Price"], color=['blue', 'green', 'red'])
        ax.set_xlabel("Car Category")
        ax.set_ylabel("Price")
        ax.set_title(f"""Total price of Different Commute Types over {Compare.PERIOD} years""")
        self.addlabels(df["Commute Type"],  df["Price"])


        st.pyplot(fig)
        st.markdown('#')
        st.text("Car Share 1: 66 euros per day and 50 km free per day. \n If you exceed 50 km you are charged at €0.25 per km.")
        st.text("Car Share 2: 55 euros per day and 50 km free per day. \n If you exceed 50 km you are charged at €0.20 per km.")
        
        multi = '''This is closely based on some of the car types found at Yuko, GOCAR and Driveyou. 
                   For different options and locations visit their sites for accurate pricing and details.
                '''
        st.markdown('#')
        st.markdown(multi)

        st.write("By Mousbah Barake. check out this [HoneyInCoffee](https://www.honeyincoffee.com/)")
        st.write("[Linkedin](https://www.linkedin.com/in/mbarake/)")

if __name__ == "__main__":
    pullsystem = UI()
    pullsystem.create_ui()