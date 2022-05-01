#Twoim zadaniem jest napisać kalkulator podatkowy.

#    Powinien on na wejściu przyjąć jedną wartość zmiennoprzecinkową: dochód.
#    Następnie powinien wyświetlić obliczony podatek, zaokrąglony do pełnych talarów. Istnieje funkcja o nazwie round() która wykona za ciebie zaokrąglenie - znajdziesz ją w szkielecie kodu w edytorze.

#Uwaga: ten szczęśliwy kraj nigdy nie zwraca pieniędzy swoim obywatelom. Jeżeli obliczony podatek jest mniejszy od zera, oznacza to tylko brak podatku (podatek jest równy zeru). Weź to pod uwagę podczas swoich obliczeń.

#Spójrz na kod w edytorze - odczytuje on tylko jedną wartość wejściową i wyświetla wynik, więc musisz ją uzupełnić pewnymi inteligentnymi obliczeniami.

dochod = float(input("Wprowadź swój roczny dochód: "))

#
# tutaj wpisz swój kod
#
if dochod <= 85528.0:   #sprawdzenie czy dochód jest mniejszy od 85528
    podatek = dochod * 0.18 - 556.02    #obliczenie podatku
    
else:
    podatek = 14839.02 + ((dochod-85528)*0.32)  #obliczenie podatku dla drugiego progu
    
if podatek <= 0:    #sprawdzenie czy obliczony podatek jest mniejszy od 0
    podatek = 0     #wtedy podatek przyjmuje wartość 0, nie może być ujemny

podatek = round(podatek, 0) #zaokrąglenie do liczby całkowitej podatku
print("Podatek wynosi:", podatek)   #wyświetlenie wyniku
