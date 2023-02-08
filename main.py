import os
#modul
import inventory
from time import sleep
import tictactoe


#Deklaration av variabler
############################################################################################################

current_room = 0

controls = '''

Kontrollerna för att spela:
Skriv [kolla] för att kolla dig omkring i rummet,
[inspektera] för att titta närmare på eventuella föremål i rummen,
[i] för att kolla vilka föremål du har(inventory),
[hjälp] för att se kontrollerna igen,

   '''
backstory = 'Du festade sent igår på en klubb. Du mådde inte så bra så att du försökte ta dig hem men du var för påverkad för att köra så du gick hem. På vägen hem ser du din farbror i en bil. Du frågar om en skjuts hem. Sen får du ett slag mot huvudet och vaknar i ett kolsvart rum. Bredvid dig finns det en ficklampa. Då inser du att du är i en källare...'

#Deklration av funktioner
############################################################################################################

def inspect(item):
   'returnerar en beskrivning av föremålet om det finns'

   #Går igenom listan med item info och kollar om föremålet finns med
   for i in item_info:
      if item == i:
         return item_info[item]

      elif item == '' or item == ' ':
         return f'Det specifierade inte vad du ville inspektera. '


      else:
         return f'Det finns ingen {item} i det här rummet. '


def split_line_print(text, seperator, sleep_tine, end='\n'):
   'Splittar "text" vid "seperator" och skriver ut en bit per rad med sleep_time tid emellan'
   for i in text.split(seperator):
      print(i, end=end)
      sleep(sleep_tine)


def events(event):
   ''
   print('Råttan utmanar dig till ett parti 3-i-rad. \nIfall du vinner säger den att du ska få nyckeln till källardörren.')
   while True:
      if 'rat' in event:
         player_input = input('Är du redo? Ja/Nej').lower()
         if 'ja' in player_input:
            if tictactoe.play(tictactoe.player, tictactoe.win) == True:
               break

         elif 'nej' in player_input:
            print('Inspektera hinken igen när du är redo')
            break
#Deklration av listot, dictionaries osv
############################################################################################################

rooms = [
  'källaren', 'trappan', 'vardagsrummet', 'hallen', 'sovrummet', 'köket',
  'garaget'
]

room_descriptions = {
  rooms[0]:
  'Du kollar runt och ser att du är i en gammal mörk källare. I källaren ser du en tavla och en hink på golvet. Det finns en dörr som leds ut ur rummet.',
  rooms[1]: 'Trappan',
  rooms[2]: 'Vardagsrummet',
  rooms[3]: 'Hallen',
  rooms[4]: 'Sovrummet',
  rooms[5]: 'Köket',
  rooms[6]: 'Garaget'
}


item_info = {
  'hink' : 'Hinken ser gammaö och rostig ut. I den hittar en råtta. event rat',
  '': '',
}



############################################################################################################





if __name__ == '__main__':
   os.system('cls')

   split_line_print(backstory, '. ', 1.3)

   sleep(2)
   os.system('cls')
   sleep(0.1)

   split_line_print('''
                  Välkommen till
   _  _  (_)(_)  __    __      __    ____  ____  _  _ §
   ( )/ )  /__\  (  )  (  )    /__\  (  _ \( ___)( \( )§
   )  (  /(__)\  )(__  )(__  /(__)\  )   / )__)  )  ( §
   (_)\_)(__)(__)(____)(____)(__)(__)(_)\_)(____)(_)\_)§''', '§', 0.1, '')

   sleep(0.25)

   split_line_print('''
                                                
                                                
                                                
            ................                  §
         ......*.,.,,,.,.,......              §
      ........,,.,,,,,,,,...........          §
      .....,,,,,**,,(.ma (.          , .       § 
      ......,,,,,***(,.((/,        * .        §
      .....,,,,,,***(. (*//*.      * ...      §
      ....,,,,,,,***(. (*//*.      / ...      §
      ......,,,,,,**(. (*//*.      / ....     §
         .......,,,,,,(. (*//*.      * .....   § 
         ....,,,,,,,/. (*//*. *    * .....    §
            ....,.,,,/. ((//*/.     * ...      §
            .. .......*. ((//*.      , ...      §
               ......*. ((//*.      , ..       §
                  ...,. */**..      .          §
                     ................          §
   ''', '§', 0.1, '')

   sleep(0.5)



   while True:
      start = input('\nStart\nAvslut\n').lower()
      if 'avslut' in start or start == 'a':
         exit()

      elif 'start' in start or start == 's':
         os.system('cls')
         break





   print(controls)

   while True:
      #if - delar upp spelarens input vid första mellanrummet så att man kan använda resten för att förstå hur spelaren vill utföra ett kommando
      #elif - kollar ifall spelaren bara klickat på enter
      #else - gör om player_input till en lista med ett tomt element. Förhindrar krashar
      player_input = input().lower()
      if ' ' in player_input:
         player_input = player_input.split(' ', 1)
      elif player_input == '':
         continue
      else:
         player_input = [player_input, '']


      print(player_input)
      #Kommandon
      ######################################################################################################
      commands = {
      'kolla': room_descriptions[rooms[current_room]],
      'hjälp' : controls,
      'inspektera': inspect(player_input[1]),
      #'i' or 'väska': inventory(),
      
      }


      ######################################################################################################

      if player_input[0] in commands:
         if 'event' in commands[player_input[0]]:
            player_input = commands[player_input[0]].split('event')
            print(player_input[0])
            events(player_input[1])
         else:   
            print(commands[player_input[0]])


      else:
         print('Det där var inget kommando. Skriv [hjälp] om du vill se vilka komandon som finns igen. ')