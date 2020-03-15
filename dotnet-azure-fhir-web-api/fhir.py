import matplotlib.pyplot as plt
from fhir_parser import FHIR
import math

fhir = FHIR()
patients = fhir.get_all_patients()

def getLanguageData():
    languages = {}
    for patient in patients:
        for language in patient.communications.languages:
            languages.update({language: languages.get(language, 0) + 1})
    print(languages)
    return languages

def getMaritalStatus():
    maritalStatus = {}
    for patient in patients:
        maritalStatus.update({str(patient.marital_status): maritalStatus.get(str(patient.marital_status), 0) + 1})
    return maritalStatus

def getAge():
    ages = {}
    for patient in patients:
        # print(math.floor(patient.age()))
        ages.update({math.floor(patient.age()/10): ages.get(math.floor(patient.age()/10), 0) + 1})
    # print(ages)
    return ages