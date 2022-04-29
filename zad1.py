#Twoim zadaniem jest przygotowanie prostego kodu, który będzie w stanie wskazać czas zakończenia dla jakiegoś przedziału czasu, podanego jako liczba minut (może być dowolnie duża). Czas rozpoczęcia podawany jest jako para godzin (0..23) i minut (0..59). Wynik musi zostać wyświetlony na konsoli.

#Na przykład, jeśli wydarzenie zaczyna się o 12:17 i trwa 59 minut, to skończy się o 13:16.

h = int(input("Czas startu (godziny): "))
m = int(input("Czas startu (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))

# wprowadź tutaj swój kod
km = ((m + d)%60) #obliczenie minuty końca wydarzenia
kg = (int(h+(m+d)/60))%24 #obliczenie godziny końca wydarzenia
print(kg, ":", km, sep="")
