import os

chain_server_url =  os.getenv("CHAIN_SERVER_URL")
if chain_server_url == "":
    raise Exception("chain server url is not set.")
print(f"chain server url: {chain_server_url}")