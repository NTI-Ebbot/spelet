import os
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
[gå] till nästa eller gå tillbaka för att gå till nästa eller det föregående rummt.
Ifall det finns flera väger kan du gå höger eller vänster.


   '''
backstory = 'Du festade sent igår på en klubb. Du mådde inte så bra så att du försökte ta dig hem men du var för påverkad för att köra så du gick hem. På vägen hem ser du din farbror i en bil. Du frågar om en skjuts hem. Sen får du ett slag mot huvudet och vaknar i ett kolsvart rum. Bredvid dig finns det en ficklampa. Då inser du att du är i en källare...'

#Deklration av funktioner
############################################################################################################

def inspect(item):
   'returnerar en beskrivning av föremålet om det finns'

   #Går igenom listan med item info och kollar om föremålet finns med
   for i in item_info[current_room]:
      if item == i:
         return item_info[current_room][item]

      elif item == '' or item == ' ':
         return f'Det specifierade inte vad du ville inspektera. \n'


   return f'Det finns ingen {item} i det här rummet. \n'


def split_line_print(text, seperator, sleep_tine, end='\n'):
   'Splittar "text" vid "seperator" och skriver ut en bit per rad med sleep_time tid emellan'
   for i in text.split(seperator):
      print(i, end=end)
      sleep(sleep_tine)

def game_over(tip):
   ''
   os.system('cls')
   split_line_print(f'''
 _____                  _____             §
|   __|___ _____ ___   |     |_ _ ___ ___ §
|  |  | .'|     | -_|  |  |  | | | -_|  _|§
|_____|__,|_|_|_|___|  |_____|\_/|___|_|  §
Tips: {tip}!                             
   ''', '§', 0.2, '')
   exit()



def events(event):
   ''
   if 'rat' in event:
      #Frågar om man vill starta 3-i-rad. Slutar när man vinner. Frågar igen om man förlorar
      print('Råttan utmanar dig till ett parti 3-i-rad. \n\nIfall du vinner säger den att du ska få nyckeln till källardörren.')
      while True:
         if 'rat' in event:
            player_input = input('Är du redo? Ja/Nej\n').lower()
            if 'ja' in player_input:
               if tictactoe.play() == True:
                  inventory.append('källarnyckel') 
                  break

            elif 'nej' in player_input:
               print('Inspektera hinken igen när du är redo')
               break

   if 'shrooms' in event:
      while True:
         player_input = input('Vill du äta dem? Ja/Nej\n').lower()
         if 'ja' in player_input:
            split_line_print('Du börjar se skumma färger och former.§Din syn börjar suddas ut.§Allting blir åter svart och du faller ihop på golvet.', '§', 1.2)
            sleep(1)
            game_over('Ät inte mystiska svampar')
         elif 'nej' in player_input:
            break
            
  if 'uncle' in event:
      while True:
         player_input = input('Vill du anfalla farbrorn? Ja/Nej\n').lower()
         if 'ja' in player_input and 'pistol' in inventory:
            split_line_print('Du riktar din pistol mot din farbrors huvud samtidigt ni stirrar varandra i ögonen.§Du sätter ett skott i hans huvud och efter ett ögonblick faller han ihop.§Hans lik är stilla på sängen och i hans ficka hittar du en nyckel till ytterdörren.', '§', 3)
            sleep(1)
            victory('Du besegrade din farbror och flydde polisen!')
         elif 'ja' in player_input:
            split_line_print('Ni stirrar var andra i ögonen.§I nästa ögonblick ger han av ett högt skrik och hoppar på dig med sina händerna på din nacke.§Allting blir svart.', '§', 3)
            sleep(1)
            game_over('Du kanske behöver ett vapen för att besegra farbrorn')
         elif 'nej' in player_input:
            print('Du kan möta honom när du är redo')
            break
            
   if 'cheese' in event:
      while True:
         print('Du öppnar kylskåpet och finner den fylld med ost.')
         player_input = input('Vill du ta upp osten? Ja/Nej\n').lower()
         if 'ja' in player_input:
            print('Undra vad du ska göra med osten?')
            inventory.append('ost') 
            break
         elif 'nej' in player_input:
            print('Osten kanske är viktig')
            break
            
   if 'painting' in evnet:
      while True:
         player_input = input('Vill du skriva in koden? Ja/Nej\n').lower()
         if 'ja' in player_input:
            player_input = input('Vad är koden?')
            if '8305' player_input:
            print('Korrekt kod. Du hittade en pistol')
            inventory.append('pistol')
            else:
            print('Inkorrekt kod')
         elif 'nej' in player_input:
            print('Det kanske finns något viktigt bakom låset')
            break


def show_inventory():
   'Returnerar vad som finns i listan "inventory" som en string'
   s = ', '.join(inventory)
   if ',' in s:
      s[s.rindex(',')] = 'och'
      return s
   elif inventory.__len__() == 0:
      return 'Du har inget'
   else:
      return s


def change_room(direction):
   'byter till rum baseat på vad spelaren'
   global current_room
   global item_info

   if current_room == 0:
      if 'nästa' in direction:
         if 'källarnyckel' in  inventory:
            current_room += 1
            return 'Du låser upp och öppnar dörren och går igenom.\n'
         else:
            return 'Dörren är låst. Du behöver en nyckel för att öppna den.\n'

   if current_room == 1:
      if 'nästa' in direction:
         current_room += 1
         return 'Du går upp för trappan och genom dörren.\n'

   if 'tillbak' in direction:
      if current_room == 1 or current_room == 2 or current_room  == 3:
         current_room -= 1
         return 'Du går tillbaka.\n'


   if current_room == 2:
      if 'höger' in direction:
         current_room += 1
         return 'Du går in genom dörren till höger.\n'
      elif 'vänster' in direction:
         current_room += 1

   if current_room == 5:
      if 'nästa' in direction:
         current_room += 1
         return 'Du går genom dörren ut ur köket.\n '
      
   return 'Det finns inget rum där eller så sa du inte vart du ville gå. \n'


#Deklration av listot, dictionaries osv
############################################################################################################

inventory = []

rooms = [
  'källaren', 'trappan', 'hallen', 'hallen2', 'sovrummet', 'köket','vardagsrummet', 'garaget'
]

room_descriptions = {
  rooms[0]:
  'Du kollar runt och ser att du är i en dammig mörk gammal källare. Förutom de mystisak svamparna i ett av hörnen ser du  en tavla och en hink på golvet. Du ser också att finns en dörr längst bort i rummet.\n',
  rooms[1]: 'Du kollar runt och är på en gammal trappa. Varje steg du tar ger ett knakande ljud. Framför dig är en dörr.\n',
  rooms[2]: 'Du står i en hall i en lång hall med alla fönster täckta av fastspikade träplankor så att det är ingen chans för dig att komma ut. Framför dig är en stort skåp. Du kan fortsäta höger eller vänster genom hallen.',
  rooms[3]: 'Du ser två dörrar, en till vänster och en till höger',
  rooms[4]: 'Du befinner dig i ett mörkt rum. Du ser din farbror sovandes på sin säng i hörnet av rummet.',
  rooms[5]: 'Du befinner dig i köket. Du ser massor av knivmärken runt hela köksväggarna. Det som står ut mest i köket är ett kylskåp.',
  rooms[6]: 'Du befinner dig i vardagsrummet där alla fönster är inspikade av träplankor. Det som står ut mest i rummet är en tavla sne tavla och en stor hylla.',
  rooms[7]: 'Du befinner dig i garaget men du ser ingen utgång. Du känner lukten bitter bensin lukt. Det som står ut mest är den blåa bilen framför dig.'
}


item_info = [{
   'tavla': 'Den föreställer fiskargubben\n',   
   'hink' : 'Hinken ser gammal och rostig ut. I den hittar en råtta. event rat',
   'svamp' : 'Det är tre små svampar. Det ser nästan ut som att de lyser i mörkret. event shrooms'
   },
   {
   'skåp' : 'Du inspekterar skåpet och hittar en bild på en vit lurvig hund. Du lägger en nämare titt och vänder på bilden och ser nummerna 8305. Du lägger en närmare titt på skåpet och hittar ett låst fack som kräver en kod.'
   },
   {},
   {
   'farbror' : 'Du går fram smyger fram mot din farbror för en närmare titt. Det sista steget du tar ger ett högt knackade ljud från trägolvet och väcker farbrorn så att han reser sig genast.'
   },
   {
   'kylskåp' : 'Du öppnar kylskåpet och finner den fylld med ost. Undra vad du kan göra med osten?'
   },
   {
   'tavla' : 'Du inspekterar tavlan av Lama. Men du märker att den inte sitter helt rätt och tar av tavlan från väggen. Bakom tavlan finner du ett skåp som kräver en kod. Vad kan koden vara?',
   'hylla' : 'Du inspekterar hyllan och finner en papperslapp. På lappen står det "Insert matte uppgift". Vad kan detta vara för?'
   },
   {}]



############################################################################################################





if __name__ == '__main__':
   os.system('cls')

   # split_line_print(backstory, '. ', 1.3)

   # sleep(2)
   # os.system('cls')
   # sleep(0.1)

   # split_line_print('''
   #                Välkommen till
   # _  _  (_)(_)  __    __      __    ____  ____  _  _ §
   # ( )/ )  /__\  (  )  (  )    /__\  (  _ \( ___)( \( )§
   # )  (  /(__)\  )(__  )(__  /(__)\  )   / )__)  )  ( §
   # (_)\_)(__)(__)(____)(____)(__)(__)(_)\_)(____)(_)\_)§''', '§', 0.1, '')

   # sleep(0.25)

   # split_line_print('''
                                                
                                                
                                                
   #          ................                  §
   #       ......*.,.,,,.,.,......              §
   #    ........,,.,,,,,,,,...........          §
   #    .....,,,,,**,,(.ma (.          , .       § 
   #    ......,,,,,***(,.((/,        * .        §
   #    .....,,,,,,***(. (*//*.      * ...      §
   #    ....,,,,,,,***(. (*//*.      / ...      §
   #    ......,,,,,,**(. (*//*.      / ....     §
   #       .......,,,,,,(. (*//*.      * .....   § 
   #       ....,,,,,,,/. (*//*. *    * .....    §
   #          ....,.,,,/. ((//*/.     * ...      §
   #          .. .......*. ((//*.      , ...      §
   #             ......*. ((//*.      , ..       §
   #                ...,. */**..      .          §
   #                   ................          §
   # ''', '§', 0.1, '')

   # sleep(0.5)



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


      #Kommandon
      ######################################################################################################
      commands = {
      'kolla': room_descriptions[rooms[current_room]],
      'hjälp' : controls,
      'inspektera': inspect(player_input[1]),
      '§': inspect(player_input[1]),
      'i' : ', '.join(inventory),
      'gå' : change_room(player_input[1]),
      
      }
      ######################################################################################################
      print(current_room)
      if player_input[0] in commands:
         if 'event' in str(commands[player_input[0]]):
            player_input = commands[player_input[0]].split('event')
            print(player_input[0])
            events(player_input[1])
         else:   
            print(commands[player_input[0]])


      else:
         print('Det där var inget kommando. Skriv [hjälp] om du vill se vilka komandon som finns igen. ')
