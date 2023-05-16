from OpenDominio import OpenDominio
from GenerateHolerite import GenerateHolerite
import time


if __name__ == '__main__':


    od = OpenDominio()
    openFolha = od.open_module('folha')

    login = LoginDominio()
    loginUser = login.userLogin(user='ROTINASDP')
    loginPassword = login.passwordLogin(password='74157')

    gh = GenerateHolerite()
    
    companiesCodes = []

    with open('../companies/companies.txt', 'r', encoding="utf8") as txtFile:
        for line in txtFile:
            line = line.strip("\n")
            companiesCodes.append(line)

    for i in companiesCodes:
        try:
            gh.dominioProcess(i)
            time.sleep(10)
        except Exception as e:
            print(f"Error processing {i}: {e}")