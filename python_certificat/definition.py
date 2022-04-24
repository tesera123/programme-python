from OpenSSL import crypto
import datetime

def lecture_du_certificat(cert_file):
    cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(cert_file).read())
    subject = cert.get_subject()
    not_after = cert.get_notAfter()
    not_before = cert.get_notBefore()
    issued_to = subject.CN    # the Common Name field
    issuer = cert.get_issuer()
    issued_by = issuer.CN

def calcul_date(date_cer):
    parse_format = "%Y%m%d"
    out_format = "%Y-%m-%d"
    not_after_byte=str(date_cer,'utf-8')
    calcul_time = datetime.datetime.strptime(not_after_byte[:8], parse_format)
    output_time_after = calcul_time.strftime(out_format)
    return output_time_after