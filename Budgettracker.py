stand = 0

while True:
    # Schleife, damit das Programm nicht frühzeitig beendet wird
    print("\n1=Hinzufügen, 2=Kontostand, 3=Beenden")
    auswahl = input("Option: ").strip()

    if auswahl == "1":
        typ = input("Typ (Einnahme/Ausgabe): ").strip()

        if typ == "Einnahme":
            betrag = float(input("Betrag: "))
            stand += betrag

        elif typ == "Ausgabe":
            betrag = float(input("Betrag: "))
            stand -= betrag

        else:
            print("Bitte wählen Sie nur zwischen 'Einnahme' und 'Ausgabe'.")

    elif auswahl == "2":
        print(f"Kontostand: {stand}")

    elif auswahl == "3":
        break

    else:
        print("Das ist keine gültige Eingabe. Bitte versuchen Sie es erneut.")


"""
while True:
    print("\n1=Hinzufügen, 2=Kontostand, 3=Beenden")
    auswahl = input("Option: ").strip()

    match auswahl:
        case "1":
            typ = input("Typ (Einnahme/Ausgabe): ").strip()
            
            if typ == "Einnahme":
                betrag = float(input("Betrag: "))
                stand += betrag
        
            elif typ == "Ausgabe":
                betrag = float(input("Betrag: "))
                stand -= betrag

            else:
                print("Bitte wählen Sie nur zwischen 'Einnahme' und 'Ausgabe'.")

        case "2":
            print(f"Kontostand: {stand}")
    
        case "3":
            break

        case _:
            print("Ihre Eingabe ist ungültig. Bitte versuchen Sie es erneut.")
"""