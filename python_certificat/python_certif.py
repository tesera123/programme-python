from OpenSSL import crypto
import datetime
from definition import *

parse_format = "%Y%m%d"
out_format = "%Y-%m-%d"

#lien : https://stackoverflow.com/questions/30862099/how-can-i-get-certificate-issuer-information-in-python

cert_file = 'C:/Users/Quentin/Desktop/python/programme-python/python_certificat/certificat_test.cer'
cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(cert_file).read())


cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(cert_file).read())
subject = cert.get_subject()
not_after = cert.get_notAfter()
not_before = cert.get_notBefore()
issued_to = subject.CN    # the Common Name field
issuer = cert.get_issuer()
issued_by = issuer.CN



# calcul de l'heure:
creation_time = calcul_date(not_before)
expiration_time = calcul_date(not_after)

print("chemin du certificat:", cert_file )
print("nom du certificat:",issued_to)
print("creer le:", creation_time)
print("expire le:", expiration_time)





