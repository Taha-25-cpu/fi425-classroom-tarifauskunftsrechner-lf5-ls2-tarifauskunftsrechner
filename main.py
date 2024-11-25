preis_erwachsene = 5.0
preis_kinder = 2.5
preis_premium = 3.0
preis_basis = 4.0
preis_keine = 5.0
preis_kinder_2 = 3.5

while True:
    print(" ### Tarifauskunftsrechner Museum XXX ### ")
    print(" Hallo, geben Sie bitte Ihr Alter ein.")
    alter_gast = int(input())

    if alter_gast < 14:
        print(" ### Eintritt Kinder ### ")
        print(" Preis: ", preis_kinder, " Euro ")
    elif 14 <= alter_gast < 18:
        print("Im alter zwischen 14-17 ist der Preis ermäßigt")
        print(" Preis: ", preis_kinder_2, " Euro ")
    else:
        print(" Sind Sie Mitglied im Duisburger Museumsclub? (Nachweis erforderlich) ")
        print(" Wenn Sie Premium-Mitglied sind, geben Sie 'p' ein.")
        print(" Wenn Sie Basis-Mitglied sind, geben Sie 'b' ein.")
        print(" Wenn Sie kein Mitglied sind, geben Sie 'k' ein. ")
        antwort_rabatt = input()
        if antwort_rabatt == "p":
            print(" ### Eintritt Premium-Mitglied ### ")
            print(" Preis: ", preis_premium, " Euro ")
            print("VIEL SPAß!!!")
        elif antwort_rabatt == "b":
            print(" ### Eintritt Basis-Mitglied ### ")
            print(" Preis: ", preis_basis, " Euro ")
            print("VIEL SPAß!!!")
        elif antwort_rabatt == "k":
            print("## Eintritt Keine Mitgliedschaft im Museumsclub ##")
            print(" Preis: ", preis_keine, " Euro ")
            print("VIEL SPAß!!!")
        else:
            print(" ### Eintritt Erwachsene (voller Preis) ### ")
            print(" Preis: ", preis_erwachsene, " Euro ")
            print("VIEL SPAß!!!")

    # Hier fragt das Programm, ob der Benutzer einen neuen Tarif berechnen möchte.
    print("Möchten Sie einen neuen Tarif berechnen? (j/n)")
    erneute_berechnung = input()
    if erneute_berechnung.lower() != 'j':
        print("Danke für die Nutzung des Tarifauskunftsrechners! Auf Wiedersehen.")
        break
