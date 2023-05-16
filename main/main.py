from OpenDominio import OpenDominio
from GenerateHolerite import GenerateHolerite


if __name__ == '__main__':


    od = OpenDominio()
    OpenFolha = od.open_module('folha')

    companiesCodes = []

    txtFile = open('../companies/companies.txt', 'r', encoding="utf8")
    for line in txtFile:
        line = line.strip("\n")
        companiesCodes.append(line)

    for element in companiesCodes:
        try:
            nav.processo(element)
            sleep(10)
        except:
            pass