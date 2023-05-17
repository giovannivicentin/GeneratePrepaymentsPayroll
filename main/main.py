from OpenDominio import OpenDominio
from GenerateHolerite import GenerateHolerite
from LoginDominio import LoginDominio
import time


if __name__ == '__main__':


    od = OpenDominio()
    openFolha = od.open_module('folha')

    lg = LoginDominio()
    loginUser = lg.userLogin(user='ROTINASDP')
    loginPassword = lg.passwordLogin(password='74157')

    gh = GenerateHolerite()
    companiesCodes = []

    with open('companies/companies.txt', 'r', encoding="utf8") as txtFile:
        for line in txtFile:
            line = line.strip("\n")
            companiesCodes.append(line)

    for i in companiesCodes:
        try:
            gh.dominioProcess(i, month='052023')
            time.sleep(10)
        except Exception as e:
            print(f"Error processing {i}: {e}")
