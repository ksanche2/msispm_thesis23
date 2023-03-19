import sys

from extract_data import *
from calc_similarity import *
from prioritize_errors import *


def main():
    report = sys.argv[1]
    req_doc = sys.argv[2]
    output_file = sys.argv[3]
    
    cpp_errors = extract_errors(report)
    if req_doc == 'owasp':
        reqs = extract_owasp('/requirement_docs/OWASP Application Security Verification Standard 4.0.3.csv')
    
    if req_doc == 'nist':
        reqs = extract_nist('/requirement_docs/SP_800-53_v5_1_XML.xml')

    sim_scores = calc_all_sim(cpp_errors, reqs)

    sorted_scores = sort_scores(sim_scores)

    write_tocsv(sorted_scores, output_file)
