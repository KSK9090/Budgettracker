stand = 0

while True:
    """Schleife damit das Programm nicht frühzeitig beendet"""
    print("\n1=Hinzufügen, 2=Kontostand, 3=Beenden")
    auswahl = input("Option: ").strip()

    if auswahl == "1":
        typ = input("Typ (Einnahme/Ausgabe): ").strip()
        betrag = float(input("Betrag: "))
        if typ == "Einnahme":
            stand += betrag
        
        elif typ == "Ausgabe":
            stand -= betrag
        else:
            print("Bitte wählen Sie nur zwischen 'Eingabe' und 'Ausgabe'.")


    elif auswahl == "2":
        print(f"Kontostand: {stand}")

    elif auswahl == "3":
        break

    else:
        print("Das ist keine gültige Eingabe. Bitte versuchen Sie es erneut unter Einbehaltung des Menüs.")


