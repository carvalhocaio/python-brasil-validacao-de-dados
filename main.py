from telefonesBr import TelefonesBr
import re

telefone = '550012345678'

telefone_objeto = TelefonesBr(telefone)
# padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
# resposta = re.search(padrao, telefone)
# print(resposta.group())

print(telefone_objeto)