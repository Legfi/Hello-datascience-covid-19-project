import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


class DataHandler:
    
    def __init__(self, country1: str, country2: str):
        """open the data file and clean it and save the user input for other function.
        this function calls two privet fanction _total and _avrage.

        Args:
            country1 ([str]): [first atribute of DataHandler]
            country2 ([str]): [second atribute of DataHandler]
        """
        
        self.my_data = pd.read_csv('~/Desktop/Data science/Project2/01_inlamningsuppgift_2_data.csv')
        self.my_data = self.my_data[['country','people_vaccinated', 'daily_vaccinations', 'people_fully_vaccinated',]]
        self.my_data_clean = self.my_data.dropna()
        
        self.country1 = country1
        self.country2 = country2
        self._total()
        self._avrage()
        
    
    def daily_vaccination(self):
        """ A public function which plot and compaire daily vaccinations situations
        """
        
        my_choosen_country1 = self.my_data_clean[self.my_data_clean['country'] == self.country1]
        my_choosen_country2 = self.my_data_clean[self.my_data_clean['country'] == self.country2]
        
        plt.plot(my_choosen_country1.people_vaccinated / 10**4, my_choosen_country1.daily_vaccinations / 10**4, label= self.country1)
        plt.plot(my_choosen_country2.people_vaccinated / 10**4, my_choosen_country2.daily_vaccinations / 10**4, label = self.country2)
        plt.xlabel('Number of vaccinated people in thousand')
        plt.ylabel('Daily number of vaccinated peaple in thousand')
        plt.legend()
        plt.show()   
        
    def full_vaccination(self):
        """ A public function which plot and compaire number of full vaccinated people
        """

        my_choosen_country1 = self.my_data_clean[self.my_data_clean['country'] == self.country1]
        my_choosen_country2 = self.my_data_clean[self.my_data_clean['country'] == self.country2]
        
        plt.plot(my_choosen_country1.people_fully_vaccinated / 10**4, my_choosen_country1.people_vaccinated / 10**4, label= self.country1)
        plt.plot(my_choosen_country2.people_fully_vaccinated / 10**4, my_choosen_country2.people_vaccinated / 10**4, label= self.country2)
        plt.xlabel('Number of vaccinated people in thousand')
        plt.ylabel('Number of fully vaccinated people in thousand')
        plt.legend()
        plt.show()
    

    def _total(self):
        """ Privet function to give extra information about the number of full vaccinated people
        """
        
        my_data_selected = self.my_data[['country', 'people_fully_vaccinated']]
        my_data_cleaned = my_data_selected.dropna()
        my_choosen_country1 = my_data_cleaned[my_data_cleaned['country'] == self.country1]
        my_choosen_country2 = my_data_cleaned[my_data_cleaned['country'] == self.country2]
        print(my_choosen_country1.iloc[-1])
        print(my_choosen_country2.iloc[-1])

    
    def _avrage(self):
        """ Privet function to give extra information about the avrage of daily vaccination
            in diffrent countries
        """
        my_data_selected = self.my_data[['country', 'daily_vaccinations']]
        my_data_selected_clean = my_data_selected.dropna()
        my_choosen_country1 = my_data_selected_clean[my_data_selected_clean['country'] == self.country1]
        my_choosen_country2 = my_data_selected_clean[my_data_selected_clean['country'] == self.country2]
        final_choice1 = my_choosen_country1.mean()
        final_choice2 = my_choosen_country2.mean()
        print(self.country1, 'avrage of', final_choice1)
        print(self.country2, 'avrage of', final_choice2)