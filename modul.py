import inventory


#Rum och föremål

############################################################################################################
current_room = 0


rooms = [
  "källaren", "trappan", "vardagsrummet", "hallen", "sovrummet", "köket",
  "garaget"
]

items_in_room = (["en hink"], [], [], [], [], [], [])



item_info = {
  "hink":
  "Du inspekterar hinken och hittar en råtta som utmanar dig på 3-i_rad. ",
  "": "",
}



room_descriptions = {
  rooms[0]:
  f"Du kollar runt och ser att du är i en gammal källare. I den ser du {', '.join(items_in_room[current_room])}",
  rooms[1]: "Trappan",
  rooms[2]: "Vardagsrummet",
  rooms[3]: "Hallen",
  rooms[4]: "Sovrummet",
  rooms[5]: "Köket",
  rooms[6]: "Garaget"
}
############################################################################################################



commands = {
  "kolla runt": room_descriptions[rooms[current_room]],
  #"insperktera": inspect(),
  "i" or "väska": inventory(),
}



