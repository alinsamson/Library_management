from datetime import datetime, date, timedelta
from random import randint

from notificare import NotificareCarte


class Persoana(object):
    '''Program sa determine datele personale ale persoanelor ce intra in contact cu biblioteca.'''
    def __init__(self, nume, prenume, varsta):
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta

    def afiseaza_persoana(self):
        print(f'Persoana: {self.nume} - {self.prenume} cu varsta de {self.varsta} a fost identificata.')


class MembruBiblioteca(Persoana):

    def __init__(self, nume, prenume, varsta, id_membru):
        super().__init__(nume, prenume, varsta)
        self.id_membru = id_membru
        #self.nrcarti_imprumutate = nrcarti_imprumutate
        self.dictionar_membri = {}
        self.lista_adrese_email = ()

    def adauga_adresa_mail(self,adresa):
        self.adresa = adresa
        self.lista_adrese_email.append(self.adresa)
        return self.lista_adrese_email



    def adauga_membru(self):
        self.dictionar_membri.update({self.nume : self.id_membru})
        return self.dictionar_membri

    def data_imprumut_carte(self, data_imprumut = date.today()):
        #data_imprumut = datetime.now()
        self.data_imprumut = data_imprumut
        return data_imprumut

    def perioada_imprumut_carte(self):
        perioada_imprumut = self.data_imprumut + timedelta(days=30)
        return perioada_imprumut


class Bibliotecar(Persoana):

    def __init__(self, nume, prenume, varsta, data_angajare):
        super().__init__(nume, prenume, varsta)
        self.data_angajare = data_angajare
        self.lista_carte_imprumutate = list()
        self.lista_intermediara = list()


    def afisare_angajare(self):
        print(f'Bibliotecarul: {self.nume} - {self.prenume} a fost angajat pe data: {self.data_angajare} .')


    def return_carte(self, carte_retur):
        self.carte_retur = carte_retur
        with open('biblioteca.txt', mode='at', encoding='UTF-8') as file4:
            file4.write('\n' + self.carte_retur)


    def disponibilitate_carte(self, carte_fizica, raspuns_imprumut = None):
        self.carte_fizica = carte_fizica
        self.raspuns_imprumut = raspuns_imprumut
        with open('biblioteca.txt', mode='rt', encoding='utf-8') as file:
            continut = file.readlines()
            for i in continut:
                a = i.rstrip('\n')
                self.lista_intermediara.append(a)

        if carte_fizica in self.lista_intermediara:
            print(f'Cartea {carte_fizica} este disponibila.')
            self.lista_intermediara.remove(self.carte_fizica)
            self.raspuns_imprumut = input('Doriti sa imprumutati cartea:')
            self.raspuns_imprumut = self.raspuns_imprumut.capitalize()

        else:
            print(f'Cartea {carte_fizica} este indisponibila.')

    def continut_biblioteca(self):
        with open('biblioteca.txt', mode='wt', encoding = 'utf-8') as file2:
            for ii in self.lista_intermediara:
                file2.write(str(ii) +'\n')


class Carte(object):
    def __init__(self, titlu, autor):
        self.titlu = titlu
        self.autor = autor

    def afisare_carte(self):
        print(f'S-a imprumutat cartea {self.titlu} scrisa de {self.autor}.')


class CarteFizica(Carte):

    def __init__(self, titlu, autor, locatie_carte, editura):
        super().__init__(titlu, autor)
        self.locatie_carte = locatie_carte
        self.status_carte = None
        self.editura = editura


def varianta2():
    try:
        print('1 - Imprumutare carte.\n2 - Returnare carte.')
        aaa = input('Apasa 1 sau 2 in functie de ce doresti sa faci:')
        if aaa =='1':
            raspuns_initial = input('Doriti sa imprumutati o carte:')
            raspuns_initial = raspuns_initial.capitalize()
            while raspuns_initial == "Da":
                date_persoane = input('Cum te numesti:')
                date_persoane = date_persoane.split(' ')
                nume = date_persoane[0]
                prenume = ''
                for i in range(1, len(date_persoane)):
                    prenume += date_persoane[i]
                data_varsta = input('Care este varsta:')
                varsta = int(data_varsta)

                solicitare_membru = input('Sunteti membru al bibliotecii:')
                solicitare_membru = solicitare_membru.capitalize()

                if solicitare_membru == 'Da':
                    print('Puteti imprumuta o carte.')
                    id_membru = int(input('Introduceti id de membru:'))
                    adresa_email_destinatar = input('Introduceti adresa de e-mail:')
                    print(('-') * 40)
                    alin = MembruBiblioteca(nume, prenume, varsta, id_membru)
                    #alin.adauga_adresa_mail(adresa_email_destinatar)
                    #print(f'Adresa de e-mail a membrului curent este:')
                    print(f'Membri biblioteca: {alin.adauga_membru()}')

                    solicitare_carte = input('Cum se numeste carte pe care doriti sa o imprumutati: ')
                    solicitare_autor = input('Care este autorul cartii:')
                    solicitare_editura = input('Care este editura:')
                    print(('-') * 40)
                    b1 = Bibliotecar('Popescu', 'Daniel', 45, '30.Nov.2005')
                    b1.afisare_angajare()
                    print(('-') * 40)
                    b1.disponibilitate_carte(solicitare_carte)
                    print(('-') * 40)
                    if b1.raspuns_imprumut == 'Da':
                        b1.continut_biblioteca()
                        a1 = CarteFizica(solicitare_carte, solicitare_autor, 'Bucuresti', solicitare_editura)
                        print(('-') * 40)
                        a1.afisare_carte()
                        print(f'Lista cu cartile imprumutate de {alin.nume} {alin.prenume}: {a1.titlu}')
                        print(('-') * 40)
                        data_de_imprumut = alin.data_imprumut_carte()
                        print(f'Cartea a fost imprumutata la data de: {data_de_imprumut.day}/{data_de_imprumut.month}/'
                              f'{data_de_imprumut.year}')
                        print('O carte se poate imprumuta pentru maxim 30 de zile.')
                        data_retur = alin.perioada_imprumut_carte()
                        print(f'Data retur carte: {data_retur.day}/{data_retur.month}/{data_retur.year}')
                        print(('-') * 40)
                        verificare_data_retur = input('Doresti sa stii daca cartea trebuie returnata:')
                        verificare_data_retur = verificare_data_retur.capitalize()
                        if verificare_data_retur == 'Da':
                            timp_actual = date.today() + timedelta(days=50)
                            print(f'Data pentru care se verifica: {timp_actual}')
                            if data_retur < timp_actual:
                                print('Cartea trebuie returnata.')
                                notificare = NotificareCarte("alinsamson1994@gmail.com",adresa_email_destinatar,
                                                             solicitare_carte)
                                notificare.trimite_notificare_mail()
                            else:
                                print('Mai poti pastra cartea.')
                else:
                    print('Nu puteti imprumuta o carte deoarece nu sunteti membru al bibliotecii.')
                    solicitare_membru = input('Doriti sa deveniti membru:')
                    solicitare_membru = solicitare_membru.capitalize()
                    if solicitare_membru == 'Da':
                        nume_membru_nou = input('Introduceti numele:')
                        nume_membru_nou = nume_membru_nou.capitalize()
                        prenume_membru_nou = input('Introduceti prenume membru nou:')
                        prenume_membru_nou = prenume_membru_nou.capitalize()
                        varsta_membru_nou = int(input('Introduceti varsta:'))
                        id_membru_nou = randint(100, 999)
                        print(f'Vi s-a alocat urmatorul id de membru: {id_membru_nou}')
                        adresa_email_destinatar = input('Introduceti adresa de e-mail:')
                        membru_nou = MembruBiblioteca(nume_membru_nou, prenume_membru_nou, varsta_membru_nou,
                                                      id_membru_nou)
                        print(f'Nou membru: {membru_nou.adauga_membru()}')
                        solicitare_carte = input('Cum se numeste carte pe care doriti sa o imprumutati: ')
                        solicitare_autor = input('Care este autorul cartii:')
                        solicitare_editura = input('Care este editura:')
                        print(('-') * 40)
                        b1 = Bibliotecar('Popescu', 'Daniel', 45, '30.Nov.2005')
                        b1.afisare_angajare()
                        print(('-') * 40)
                        b1.disponibilitate_carte(solicitare_carte)
                        print(('-') * 40)
                        if b1.raspuns_imprumut == 'Da':
                            b1.continut_biblioteca()
                            a1 = CarteFizica(solicitare_carte, solicitare_autor, 'Bucuresti', solicitare_editura)
                            print(('-') * 40)
                            a1.afisare_carte()
                            print(f'Lista cu cartile imprumutate de {membru_nou.nume} {membru_nou.prenume}: {a1.titlu}')
                            print(('-') * 40)
                            data_de_imprumut = membru_nou.data_imprumut_carte()
                            print(
                                f'Cartea a fost imprumutata la data de: {data_de_imprumut.day}/{data_de_imprumut.month}/'
                                f'{data_de_imprumut.year}')
                            print('O carte se poate imprumuta pentru maxim 30 de zile.')
                            data_retur = membru_nou.perioada_imprumut_carte()
                            print(f'Data retur carte: {data_retur.day}/{data_retur.month}/{data_retur.year}')
                            print(('-') * 40)
                            verificare_data_retur = input('Doresti sa stii daca cartea trebuie returnata:')
                            verificare_data_retur = verificare_data_retur.capitalize()
                            if verificare_data_retur == 'Da':
                                timp_actual = date.today() + timedelta(days=50)
                                print(f'Data pentru care se verifica: {timp_actual}')
                                if data_retur < timp_actual:
                                    print('Cartea trebuie returnata.')
                                    notificare = NotificareCarte("alinsamson1994@gmail.com", adresa_email_destinatar,
                                                                solicitare_carte)
                                    notificare.trimite_notificare_mail()
                                else:
                                    print('Mai poti pastra cartea.')

                    else:
                        print('Nu puteti imprumuta o carte.')
                        break
                raspuns_initial = input('Doriti sa imprumutati o alta carte:')
                raspuns_initial = raspuns_initial.capitalize()
        else:
            # print('Vreau sa returnez o carte.')
            b1 = Bibliotecar('Ramon', 'Daniel', 45, '30.Nov.2005')
            carte_de_returnat = input('Ce carte vrei sa returnezi:')
            b1.return_carte(carte_de_returnat)
            print('Va multumim pentru retur.')

    except Exception as eroare_creata:
        print(f'Datele introduse nu sunt corecte.Eroare - {eroare_creata}')


if __name__ == '__main__':
    varianta2()

