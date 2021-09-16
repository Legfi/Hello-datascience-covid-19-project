


from DataHandler import DataHandler
import argparse

def main(country1:str, country2:str , daily: bool, full: bool):
    """main function which calls difrrent public and privet functions depending on users input

    Args:
        country1 (str): [first country]
        country2 (str): [second country]
        daily (bool): [a boolian to show informations about daily vaccinations in difrrent countries]
        full (bool): [a boolian to show informations about number of fully vaccinated peaple]
    """

    if daily:
        try:
            data_handler = DataHandler(country1, country2)
            data_handler.daily_vaccination()
        except IndexError:
            print("unfortunately there isn't any data available! check your spelling!")
    elif full:
        try:
            data_handler = DataHandler(country1, country2)         
            data_handler.full_vaccination()
        except IndexError:                
            print("unfortunately there isn't any data available! check your spelling and try again!")
    else: 

        print("unfortunately there isn't any data available! check your spelling and try again!")
        
if __name__ == "__main__":
    """this main fuction asks for two country as input and gives 2 alternative to choose daily or full
    """

    parser = argparse.ArgumentParser(description='getting countries that user want to analise')
    parser.add_argument('--country1' , help ='first country please!', required=True, type=str.capitalize)
    parser.add_argument('--country2' , help ='second country please!', required=True, type=str.capitalize)
    parser.add_argument('--daily' , dest='daily', action='store_true', help='shows how many people get vaccine every day')
    parser.add_argument('--full', dest='full', action='store_true', help=' shows the number of full vaccinated people')
    parser.set_defaults(daily=False)
    parser.set_defaults(full =False)

    args = parser.parse_args()
    country1 = args.country1
    country2 = args.country2
    daily = args.daily
    full = args.full

    main(country1, country2, daily, full)
