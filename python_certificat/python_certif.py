from wsgiref.simple_server import WSGIRequestHandler
from OpenSSL import crypto
import OpenSSL.crypto
import datetime
from definition import *
from cryptography import x509
import os
from subprocess import call
import glob
import csv
import operator

date = datetime.datetime.today().date()
print(date)

#lien : https://stackoverflow.com/questions/30862099/how-can-i-get-certificate-issuer-information-in-python
#lien : https://www.pyopenssl.org/en/stable/api.html

#cert_test = "C:/Users/Quentin/Desktop/certificat/test/www.carsat-bretagne.fr.cer"
recherche_cer =r'C:\Users\Quentin\Desktop\certificat'
file_txt = r'C:\Users\Quentin\Desktop\python\programme-python\python_certificat\cer_txt.csv'
file_trier = r'C:\Users\Quentin\Desktop\python\programme-python\python_certificat\cer_sort.csv'

text_files = glob.glob(recherche_cer + "/**/*.cer", recursive = True)
print(text_files)
list_cer = []

for i in text_files:
    try:
        path_certif = i
        cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(path_certif).read())
        subject = cert.get_subject()
        not_after = cert.get_notAfter()
        not_before = cert.get_notBefore()
        issued_to = subject.CN    # the Common Name field
        issuer = cert.get_issuer()
        issued_by = issuer.CN
        extension = cert.get_extension_count()
        affichage_extension = cert.get_extension(int(extension)-1)

        # calcul de l'heure:
        creation_time = calcul_date(not_before)
        expiration_time = calcul_date(not_after)
        expiration_day = calcul_day(expiration_time)

        print("*****************************")
        #print("extension:", extension)
        #print("subject:", subject)
        print("issued:", issued_by)
        print("chemin du certificat:", path_certif )
        print("nom du certificat:",issued_to)
        #print("creer le:", creation_time)
        print("expire le:", expiration_time)
        print("jour avant expiration:", expiration_day )
        print("*****************************")

        ecriture_msg = issued_by + ';' + path_certif + ';' + issued_to + ';' + str(expiration_day)
        list_cer.append(ecriture_msg)
        fichier = open(file_txt, "a")
        fichier.write(ecriture_msg + '\n')
        fichier.close()
        list_cer[ecriture_msg]


    except:
        print("/!\ attention: erreur sur ",path_certif)


sample = open(file_txt,'r')
csv1 = csv.reader(sample,delimiter=';')
sort = sorted(csv1,key=operator.itemgetter(2))

for eachline in sort:
    print(eachline)