# STATS401-Project2

DKU STATS401 Project II

A Glance into NFT Ethics: On Ethics of CryptoPunk

> Authors: Yufan Zhang and Zichao Chen

![1652455511555.png](poster.png)

## Repo structure

```
project
│   README.md
│   requirements.txt
│
└───data
│   │   punk_imgs/
│   │   wc_imgs/
│   │   vis4_data/
│   │   vis1_data.json
│   │   data2_final.csv
│   │   vis3_data.csv
│   │   vis5_data.csv
│   │   vis5_df_sa.csv
│   │   vis5_all_tweet_content.txt
│   
└───main    # codes for data acquisition
│   │   queryDune.py
│   │   scrapeTweets.ipynb
│   │   database.ipynb
│   │
│   └───apps    # codes for visualization
│   │   │   app_vis1.py
│   │   │   vis2.html
│   │   │   echarts.js
│   │   │   app_vis3.py
│   │   │   app_vis4.py
│   │   │   app_vis5.py
│   │
│   └───vis_data_clean  # code for data cleaning, and engineering
│   │   │   vis1.ipynb
│   │   │   vis2.ipynb
│   │   │   vis3.ipynb
│   │   │   vis4.ipynb
│   │   │   vis5.ipynb
│   │
│   └───ori_data
│   │   │   punkBought_{date}.json
│   │   │   punkTransfer_{date}.json
│   │
│   └───database
│       │   punk_db.csv
│       │   trader_db.csv
│       │   tweets_db.csv
│       │   tx_db.csv
```

## How to use

### Create a new environment and install packages

```bash
conda create vis
conda activate vis
pip install -r requirements.txt
```

### Query data

from [dune](https://dune.com/browse/dashboards)

```bash
cd ./main
python queryDune.py
```

from [Twitter](https://twitter.com/)

```bash
scrapeTweets.ipynb
```

### (Vis1, Vis3-5) Build App with Ployly Dash

```bash
cd ./main/apps
python app_vis1.py
python app_vis3.py
python app_vis4.py
python app_vis5.py
```

### (Vis2) Open the vis2.html with Live Server

## Dataset

### Raw data from data querying

```bash
cd ./main/ori_data
```

### Cleaned database

```bash
cd ./main/database
```

### Dataset for visualization after data engineering

```bash
cd ./data
```
