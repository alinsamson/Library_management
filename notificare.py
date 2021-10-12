class NotificareCarte(object):

    def __init__(self, adresa_expeditor, adresa_destinatar, carte_retur):
        self.adresa_expeditor = adresa_expeditor
        self.adresa_destinatar = adresa_destinatar
        self.carte_retur = carte_retur


    def trimite_notificare_mail(self):
        import smtplib
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.adresa_expeditor, 'Ramirez101!')
        subject = 'Termen imprumut carte depasit'
        body = '''Buna ziua,
Va aducem la cunostinta ca ati depasit termenul limita de imprumut al cartii {0}.
Va rugam sa o returnati cat mai curand posibil.
Biblioteca Nationala'''.format(self.carte_retur)
        mesaj = "Subject: {}\n\n{}".format(subject, body)
        server.sendmail(self.adresa_expeditor, self.adresa_destinatar, mesaj)
        print('E-mail transmis cu succes.')
        server.quit()

if __name__ == '__main__':
    notificare = NotificareCarte("alinsamson1994@gmail.com", "alinsamson1994@gmai.com")
    notificare.trimite_notificare_mail()
