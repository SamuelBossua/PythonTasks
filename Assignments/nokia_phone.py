def main_menu():
  while True:
   print("----------NOKIA 3310-----------")
   print("1. Phone Book")
   print("2. Messages")
   print("3. Chat")
   print("4. Call register")
   print("5. Tones")
   print("6. Settings")
   print("7. Call Divert")
   print("8. Games")
   print("9. Calculator")
   print("10. Reminders")
   print("11. Clock")
   print("12. Profiles")
   print("13. SIM Services")
   print("0. Exit")

   select = input("Enter a number: ")
   
   match select:
    case "1" : 
     phone_book()
    case "2" :
     print("loading messages......")
    case "3" :
     print("opening chat........")
    case "4" :
     print("Opening Call Register.......")
    case "5" :
     print("opening tones......")
    case "6" :
     print("opening settings.......")
    case "7" :
     print("opening call divert......")
    case "8" :
      print("Opening Games...")
    case "9":
      print("Opening Calculator...")
    case "10":
      print("Opening Reminders...")
    case "11":
      print("Opening Clock...")
    case "12":
      print("Opening Profiles...")
    case "13":
      print("Opening SIM Services...")
    case "0":
      print("Phone switched off.")
      break
    case _:
      print("Invalid choice. Try again.")

def phone_book():
 while True:
  print("\n--- PHONE BOOK ---")
  print("1. Search")
  print("2. Service Nos.")
  print("3. Add Name")
  print("4. Erase")
  print("5. Edit")
  print("6. Assign Tone")
  print("7. Send b'card")
  print("8. Options")
  print("9. Speed Dials")
  print("10. Voice Tags")
  print("0. Back")

  select = input("Choose an option: ")

  match select:
   case "1":
    print("Search")
   case "2":
    print("Service Nos.")
   case "3":
    print("Add Name")
   case "4":
    print("Erase")
   case "5":
    print("Edit")
   case "6":
    print("Assign Tone")
   case "7":
    print("Send b'card")
   case "8":
    phone_book_options()
   case "9":
    print("Speed Dials")
   case "10":
    print("Voice Tags")
   case "0":
    break
   case _:
    print("Invalid choice. Try again.")

def phone_book_options():
 while True:
  print("\n--- PHONE BOOK OPTIONS ---")
  print("1. Type of View")
  print("2. Memory Status")
  print("0. Back")

  select = input("Choose an option: ")

  match select:
   case "1":
    print("Type of View")
   case "2":
    print("Memory Status")
   case "0":
    break
   case _:
    print("Invalid choice. Try again.")   






main_menu()














