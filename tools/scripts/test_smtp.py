#!/usr/bin/env python

import smtplib
import ssl


tls_versions = [ssl.PROTOCOL_TLS, ssl.PROTOCOL_TLSv1, ssl.PROTOCOL_TLSv1_1, ssl.PROTOCOL_TLSv1_2]
host = '<REPLACE_WITH_YOUR_SMTP_HOST>'
port = <REPLACE_WITH_YOUR_SMTP_PORT>

for tls in tls_versions:
    s = smtplib.SMTP(host, port)
    s.set_debuglevel(2)
    print('-' * 10)
    c = ssl.SSLContext(tls)
    try:
        print(tls)
        s.ehlo()
        s.starttls(context=c)
        s.close()
    except Exception as e:
        print('=' * 10)
        print('>>> {}: {}'.format(tls.__repr__, e))
        print('=' * 10)
        s.close()

print('-' * 10)
try:
    s = smtplib.SMTP(host, port)
    s.set_debuglevel(2)
    print('Default TLS')
    s.ehlo()
    s.starttls()
    s.close()
except Exception as e:
    print('=' * 10)
    print('>>> Default TLS: {}'.format(e))
    print('=' * 10)

#
# [EOF]
#
