from bs4 import BeautifulSoup
import pandas as pd 

def extract_errors(report_file):
    with open(report_file, 'r') as f:
        cdata = f.read()
    cpp_data = BeautifulSoup(cdata, 'xml')

    cpp_errors = cpp_data.find_all('error')
    cpp_err = []
    for e in cpp_errors:
        cpp_err.append(e['msg'])
    
    return cpp_err

def extract_nist(reqs_file):
    with open(reqs_file, 'r') as f:
        rdata = f.read()
    req_data = BeautifulSoup(rdata, 'xml')
    # limit to relevant NIST control families
    rmf_reqs = []
    for x in req_data.find_all('statement'):
        if x.find('number') is not None:
            if 'AC' or 'CA' or 'CM' or 'IA' or 'RA' or 'SI' in x.find('number').text:
                rmf_reqs.append(x.find('description').text)

    return rmf_reqs

def extract_owasp(reqs_file):
    owasp = pd.read_csv(reqs_file)
    owasp_reqs = owasp['req_description']
    return owasp_reqs

