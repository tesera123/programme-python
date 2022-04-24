from OpenSSL import crypto
from def import *

#lien : https://stackoverflow.com/questions/30862099/how-can-i-get-certificate-issuer-information-in-python

cert_file = 'C:/Users/Quentin/Desktop/python/programme-python/python_certificat/certificat_test.cer'
cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(cert_file).read())

lecture_du_certificat(cert_file)

print("subject: ", subject)
print("not_after: ", not_after)
print("issued_to: ", issued_to)
print("issuer: ", issuer)
print("issued_by: ", issued_by)