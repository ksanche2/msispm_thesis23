import pandas as pd

def sort_scores(sim_scores):
    sorted_max = sorted(sim_scores, reverse=True)
    sorted_dict = {i: sim_scores[i] for i in sorted_max}

    return sorted_dict

def write_tocsv(sorted_err, output_file):
    df = pd.DataFrame(list(sorted_err.items()),
                      columns=['error message', 'similarity score'])
    
    df.to_csv(output_file, index=False, header=True)