#pyta sie co chesz dodac typu wpisz cena/użytkownik/przedmiot/data
#potem wpisuje to do biblioteki ze cena: 80 / uzytkownik: igor/ przedmiot: monitor/ data: 25-09-2137
library = {}
print("napisz <wpisz> by dodać wartość do kluczy")
print("napisz <zmień> by zmienić zawartość danego klucza")
print("napisz <usuń> by usunąć zawartość danego klucza")
print("napisz <pokaż> by pokazać zawartość danego klucza lub wszystkie klucze")
print("napisz <koniec> by zakończyć proces")
print("-----------------------------------------------------------------------")
while True:
    query_value = input("ustaw index: ")
    if query_value == "koniec":
        break
    elif query_value == "wpisz":
        insert_value = input("do czego chcesz wpisać dane: ")
        if insert_value not in library:
            print("nie ma takiego indexu")
            continue
        search_value = input("wpisz wartość: ") 
        library[insert_value] = search_value
        continue
    elif query_value == "zmień":
        change_value = input("do czego chcesz zmnienić dane: ")
        if change_value not in library:
            print("nie ma takiego indexu")
            continue
        search_value = input("wpisz nową wartość: ")
        library[change_value] = search_value
    elif query_value == "usuń":
        delete_value = input("do czego chcesz usunąć dane (dana zawartość / <cały> ): ")
        if delete_value == "cały":
            question_delete = input("jaki klucz chcesz usunąć: ")
            if question_delete not in library:
                print("nie ma takiego klucza")
            else:
                del library[question_delete]
            continue
        if delete_value not in library:
            print("nie ma takiego indexu")
            continue
        else:
            library[delete_value] = None
    elif query_value == "pokaż":
        show_value = input("do czego chcesz zobaczyć dane (dany klucz / <wszystkie> ): ")
        if show_value == "wszystkie":
            print(library)
        elif show_value not in library:
            print("nie ma takiego indexu")
            continue
        else:
            print(library[show_value])
    else:
        library[query_value] = None
print(library)