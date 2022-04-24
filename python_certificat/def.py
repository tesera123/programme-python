from OpenSSL import crypto

def lecture_du_certificat(cert_file):
    cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(cert_file).read())
    subject = cert.get_subject()
    not_after = cert.get_notAfter()
    not_before = cert.get_notBefore()
    issued_to = subject.CN    # the Common Name field
    issuer = cert.get_issuer()
    issued_by = issuer.CN