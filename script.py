import csv  # See rida impordib mooduli, mis aitab lugeda CSV faile.

class Item:  # See on nagu asjade mall, mille abil saab luua uusi asju.
    pay_rate = 0.8  # See on allahindlus, mida rakendatakse kõikidele asjadele.
    all = []  # See on nimekiri, kuhu pannakse kõik loodud asjad.

    def __init__(self, name: str, price: float, quantity=0):  # See on nagu salajane kood, mis käivitub automaatselt, kui uus asi luuakse.
        # Kontrollime, kas hind ja kogus on õiged.
        assert price >= 0, f"Hind {price} ei tohi olla negatiivne!"
        assert quantity >= 0, f"Kogus {quantity} ei tohi olla negatiivne!"

        # Anname asjale nime, hinna ja koguse.
        self.name = name
        self.price = price
        self.quantity = quantity

        # Lisame asja nimekirja.
        Item.all.append(self)

    def calculate_total_price(self):  #See kood arvutab asja koguhinna.
        return self.price * self.quantity

    def apply_discount(self):  #See kood rakendab asjale allahindlust.
        self.price = self.price * self.pay_rate

    @classmethod  #See on kood, mis loeb asjade andmed CSV failist ja loob nende põhjal uusi asju.
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:  #Avame CSV faili.
            reader = csv.DictReader(f)  #Loeme faili sisu.
            items = list(reader)  # Teeme faili sisust listi.

        for item in items:  #Käime läbi kõik asjad listis.
            Item(  # oome iga asja kohta uue asja.
                name=item.get('name'),  # Loeme asja nime failist.
                price=float(item.get('price')),  # Loeme asja hinna failist ja muudame selle numbriks.
                quantity=int(item.get('quantity')),  # Loeme asja koguse failist ja muudame selle täisarvuks.
            )

    @staticmethod  # See on funktsioon, mis kontrollib kas arv on täisarv.
    def is_integer(num):
        #Kontrollin, kas arv on täisarv või komaga arv mille komakoht on ,0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):  # See kood näitab kuidas asja nimi välja näeb, kui seda kuskil kuvatakse.
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    