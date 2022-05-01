#!/usr/bin/python

import datetime
import glob
import subprocess
import os

from OpenSSL import crypto

def calcul_date(date_cer):
    parse_format = "%Y%m%d"
    out_format = "%Y-%m-%d"
    not_after_byte=str(date_cer,'utf-8')
    calcul_time = datetime.datetime.strptime(not_after_byte[:8], parse_format)
    output_time_after = calcul_time.strftime(out_format)
    return output_time_after

def calcul_day(date_certificat):
    date_today = datetime.datetime.today().date()
    d1_converted = datetime.datetime.strptime(str(date_today),'%Y-%m-%d')
    d2_converted = datetime.datetime.strptime(date_certificat,'%Y-%m-%d')
    day = (d2_converted - d1_converted).days
    print(day)

#lien : https://stackoverflow.com/questions/30862099/how-can-i-get-certificate-issuer-information-in-python
#lien : https://www.pyopenssl.org/en/stable/api.html

path_coffre = '/opt/certificats_controle/mntcert'
path_recherche = path_coffre + '/Certificats'

print('********')
print("***check du mount sur le serveur linux***")
check_file = os.path.isdir('/opt/certificats_controle/mntcert/Certificats')
if check_file != "true":
    print("montage CIFS non présent, mount sur le repertoire:", path_coffre)
    proc = subprocess.Popen(['sudo','mount','-t','cifs','-o','credentials=/opt/certificats_controle/credentials','//srvficor.infra.n18.an.cnav/CNP_DATA/Coffre/COMMUN','/opt/certificats_controle/mntcert'])
else:
    print("montage CIFS présent sur le repertoire:", path_coffre)

print('********')
print("recherche des certificats avec l'extension.cer")
text_files = glob.glob(path_recherche + "/**/*.cer", recursive = True)
print(text_files)
print('********')

# for path,path_files,path_files_name in os.walk(path_recherche):
#     for item in path_files_name:
#         if item.endswith('.cer'):
#             path_certificat_cifs = path + '/' + item


var_chemin = "/opt/certificats_controle/mntcert/Certificats/CERTIGNA/demande-autonomie.fr/2022-06-24_demande-autonomie.fr.cer"
cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(var_chemin).read())
subject = cert.get_subject()
not_after = cert.get_notAfter()
not_before = cert.get_notBefore()
issued_to = subject.CN
issuer = cert.get_issuer()
issued_by = issuer.CN
extension = cert.get_extension_count()
affichage_extension = cert.get_extension(int(extension)-1)

# calcul de l'heure:
#creation_time = calcul_date(not_before)
#expiration_time = calcul_date(not_after)
#day_expiration = calcul_day(expiration_time)

print("*****************************")
#print("extension:", extension)
#print("subject:", subject)
print("issued:", issued_by)
print("chemin du certificat:", var_chemin )
print("nom du certificat:",issued_to)
#print("creer le:", creation_time)
#print("expire le:", expiration_time)
#print("jour avant expiration:",day_expiration )
print("*****************************")
