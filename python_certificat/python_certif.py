from OpenSSL import crypto
import datetime
from definition import *
from cryptography import x509
import os
import subprocess


#lien : https://stackoverflow.com/questions/30862099/how-can-i-get-certificate-issuer-information-in-python
#lien : https://www.pyopenssl.org/en/stable/api.html

cert_file = 'C:/Users/Quentin/Desktop/python/programme-python/python_certificat/certificat_test.cer'




cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(cert_file).read())
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

print("*****************************")
#print("extension:", extension)
#print("subject:", subject)
print("issued:", issued_by)
print("chemin du certificat:", cert_file )
print("nom du certificat:",issued_to)
#print("creer le:", creation_time)
print("expire le:", expiration_time)
print("*****************************")
