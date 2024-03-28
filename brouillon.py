from dotenv import load_dotenv
import os
from constants import (START_BLOCK, 
                       BALANCER_VAULT_CONTRACT, 
                       COW_AMM_ADDRESS, 
                       ORIGINAL_BLOCK, 
                       BALANCER_SWAP_TOPIC,
                       SCAN,
                       END_BLOCK,
                       BALANCER_POOL_TOPIC,)
i=1

load_dotenv()
SCAN_API_KEY = os.getenv("GNOSISSCAN_KEY")
start_block = ORIGINAL_BLOCK + 1
url = (
            "https://api."
            + SCAN
            +".io/api?module=account&action=tokentx&address="
            + COW_AMM_ADDRESS
            + "&startblock="
            + str(start_block)
            + "&endblock="
            + str(END_BLOCK)
            +"&sort=asc"
            + "&page="
            + str(i)
            + "&offset=1000&apikey="
            + SCAN_API_KEY
        )

print(url)

a=2
def f():
    print(a)

f()


import datetime

date_string = "2024-02-26 05:26:45"
date_format = "%Y-%m-%d %H:%M:%S"

date = datetime.datetime.strptime(date_string, date_format)
epoch = datetime.datetime(1970, 1, 1)

seconds_since_epoch = (date - epoch).total_seconds()

print(seconds_since_epoch)

#0xDE8C195AA41C11A0C4787372DEFBBDDAA31306D2000200000000000000000181
#0XB8BB1CE9C6E5401D66FE2126DB6E7387E1E24FFE -> get it from the url of the balancer pool
#0xb8bb1ce9c6e5401d66fe2126db6e7387e1e24ffe00020000000000000000003d
# from https://app.balancer.fi/#/gnosis-chain/pool/0xb8bb1ce9c6e5401d66fe2126db6e7387e1e24ffe00020000000000000000003d
# or via gnosisscan -> logs -> swap event -> topic

# 0xBA12222222228d8Ba445958a75a0704d566BF2C8
#small change
print("0xb8bb1ce9c6e5401d66fe2126db6e7387e1e24ffe00020000000000000000003d".upper())