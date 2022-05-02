import time

def get_page():
    print("Starting to download page")
    time.sleep(1)
    print("Done downloading page")
    return "<html>Hello</html>"

def read_db():
    print("Starting to retrieve data from db")
    time.sleep(0.5)
    print("Connected to db")
    time.sleep(1)
    print("Done retrieving data from db")
    return "db-data"

def run():
    start = time.time()
    get_page()
    read_db()
    #print(f"Time elapsed: {time.time()-start:.3}s")
