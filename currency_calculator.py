
import requests, json


class Calculator(): 
    def __init__(self):
        self.api_key = "my API key"
        self.base_url = "https://api.exchangerate-api.com/v4/latest/"
        self.history = [] #a list to collect all currency conversions 

        self.menu = {
            1:("Przelicz kwote na dowolna walute", self.convert_currency),
            2:("Zapisz historię do pliku", self.save_history),
            0:("Zamknij", self.exit)
        }
    
    def show_menu(self):
        print("\n" + "="*30)
        print("       KALKULATOR WALUT")
        print("="*30)
        for key, (description,_) in self.menu.items():
            print(f"{key}. {description}")
        print("="*30)


    #currency converter
    def convert_currency(self):
        print("\n--- KONWERSJA WALUT ---")

        #getting from_currency and to_currency
        from_currency = input("Z jakiej waluty? (np. USD): ").upper()
        to_currency = input("Na jaką walutę? (np. EUR): ").upper() 
        

        #getting amount to convert, checking if amount is a correct number
        try:
            amount = float(input("Podaj kwotę: "))  
        except ValueError:
            print("Błąd! Podaj prawidłową kwotę.")
            return

        #API call to get the current rates
        try:
            url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
            response = requests.get(url, timeout=5)
            data = response.json()   
            
            response.raise_for_status() #check if response 200
            
            #getting rate for a selected currency
            currency_rate = data["rates"][to_currency]

            #conversion result
            result = float(amount) * float(currency_rate)
        
            #text result           
            print(f"\n{amount} {from_currency} = {result:.2f} {to_currency}")           #:.2f for float 2 numbers after '.'
            print(f"    Kurs: 1 {from_currency} = {currency_rate:.4f} {to_currency}")   #:.4f for float 4 numbers after '.'
            
            #save to history []
            self.history.append({
            "kwota": amount,
            "z_waluty" : from_currency,
            "na_walute": to_currency,
            "wynik" : result,
            "kurs": currency_rate
        })

        except requests.exceptions.RequestException as e:
            print(f"Bład polaczenia z API: {e}")
            
        except KeyError:
            print("Bład w odpowiedzi API")        
            
    
    #saving history to a json file
    def save_history(self):
        if not self.history:
            print("Brak historii do zapisania!")
            return False
        
        try:
            with open(f"C:/python/currency/history.json", "w", encoding="utf-8") as f:
                json.dump(self.history, f, ensure_ascii=False, indent=2)
                print("Zapisano do pliku C:/python/currency/history.json")
            return True
        except IOError:
            print("Bład podczas zapisywania pliku.")
            return False

    #program exit
    def exit(self):
        print("n\n💾 Zapisuje historie...")
        if self.save_history():
            print("✅ Historia zapisana!")
        print("👋Zamykam...Do widzenia!")
        import sys
        sys.exit(0)




    def run(self):
        """Main loop"""

        print("\nWitaj w kalkulatorze!")

        while True:
            self.show_menu()

            try:
                choice = int(input("\n Wybierz opcje: "))

                #check if option exist:
                if choice not in self.menu:
                    print("Nieprawidlowa opcja! Wybierz z menu")
                    continue
                #wyjscie
                if choice == 0:
                    print("\n Do widzenia!")
                    break

                #run selected method
                description, method = self.menu[choice]
                if method:
                    method()
            except ValueError:
                print("Podaj liczbe z menu!")

            except KeyboardInterrupt:
                print("\n\n 👋Program przerwany. Do widzenia!")
                break

#Run
if __name__ == "__main__":
    calc = Calculator()
    calc.run()