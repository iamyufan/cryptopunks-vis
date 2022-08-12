from duneanalytics import DuneAnalytics
import time
import json


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


DUNE_DATA_PATH = './dune_data'


def save_data(dune_dict, file_predix, DUNE_DATA_PATH=DUNE_DATA_PATH):
    """
    Write data to json file
    """
    from datetime import date
    today = str(date.today())
    out_file = '{}/{}_{}.json'.format(DUNE_DATA_PATH, file_predix, today)
    with open(out_file, 'w') as f:
        json.dump(dune_dict, f)
    print('===== Data saved to {} ====='.format(out_file))


dune_bt_dict = query_data_from_dune('punkBought')
save_data(dune_bt_dict, 'punkBought')

# dune_tf_dict = query_data_from_dune('punkTransfer')
# save_data(dune_tf_dict, 'punkTransfer')
