import os
#modul
import inventory
from time import sleep
if __name__ == "__main__":
   os.system('cls')

   print('''
                  Välkommen till
   _  _  (_)(_)  __    __      __    ____  ____  _  _ 
   ( )/ )  /__\  (  )  (  )    /__\  (  _ \( ___)( \( )
   )  (  /(__)\  )(__  )(__  /(__)\  )   / )__)  )  ( 
   (_)\_)(__)(__)(____)(____)(__)(__)(_)\_)(____)(_)\_)''')

   print('''
                                                
                                                
                                                
            ................                  
         ......*.,.,,,.,.,......              
      ........,,.,,,,,,,,...........          
      .....,,,,,**,,(.ma (.          , .        
      ......,,,,,***(,.((/,        * .        
      .....,,,,,,***(. (*//*.      * ...      
      ....,,,,,,,***(. (*//*.      / ...      
      ......,,,,,,**(. (*//*.      / ....     
         .......,,,,,,(. (*//*.      * .....    
         ....,,,,,,,/. (*//*. *    * .....    
            ....,.,,,/. ((//*/.     * ...      
            .. .......*. ((//*.      , ...      
               ......*. ((//*.      , ..       
                  ...,. */**..      .          
                     ................          
   ''')


   while True:
      start = input("\nStart\nAvslut\n").lower()
      if "avslut" in start or start == "a":
         exit()

      elif "start" in start or start == "s":
         break

   print("")

   while True:
      print("a")
      response = input()
