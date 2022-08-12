from duneanalytics import DuneAnalytics
import time
import json
import os

    
def query_data_from_dune(data_mode):
    """
    Query data from Dune Analytics
    """
    # initialize client
    dune = DuneAnalytics('brucezzzzzzzyf@gmail.com', 'ZHANG0509yf')

    # try to login
    dune.login()

    # fetch token
    dune.fetch_auth_token()

    # set query ids
    if data_mode == 'punkBought':
        query_dict = {'2017': 673785,
                      '2018': 673784,
                      '2019': 673783,
                      '2020': 673781,
                      '2021': 673779,
                      '2022': 673771}
    elif data_mode == 'punkTransfer':
        query_dict = {'2017-2019': 674456,
                      '2020': 674472,
                      '2021': 674496,
                      '2022': 674500}

    # query data
    dune_data = {}
    for year in query_dict:
        query_id = query_dict[year]
        result_id = dune.query_result_id(query_id=query_id)
        dune_data[year] = dune.query_result(result_id)
        time.sleep(5)

    return dune_data


def save_data(dune_dict, file_predix, save_path):
    """
    Write data to json file
    """
    from datetime import date
    today = str(date.today())
    out_file = '{}/{}_{}.json'.format(save_path, file_predix, today)
    with open(out_file, 'w') as f:
        json.dump(dune_dict, f)
    print('===== Data saved to {} ====='.format(out_file))
    
    
def main(args):
    RAW_DATA_PATH = '../data/ori'
    if os.path.exists(RAW_DATA_PATH) is False:
        os.makedirs(RAW_DATA_PATH)
        
    data_mode = args.data_mode
    dune_dict = query_data_from_dune(data_mode)
    save_data(dune_dict, data_mode, RAW_DATA_PATH)

    
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Query TX from Dune')
    
    parser.add_argument('--data-mode', type=str, default='punkBought')
    args = parser.parse_args()

    main(args)
