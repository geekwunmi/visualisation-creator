import pandas as pd
import seaborn as sns

login_details = {
    "username":""
,   "password":""
,   "warehouse":""
,   "schema":""
}

connection_details = []

sql = {"non-numeric":""
       ,"numeric":""
       ,"table_name":""
       ,"date_range":""
       ,"filter_fields":""
       }
sql_ready = [""]


# collect user details to create connection
def collect_details():
    for key in login_details.keys():
        print(key + "?")
        response = input("> ")
        login_details[key] = response
    return print(login_details)

# collect sql from user
def collect_sql():
    options =["y","n"]
    print("Lets build your sql!")
    print("would you like to build your query?")
    print(options)

    build_query = input("> ")
    if build_query == "n":
        sql_ready = input("> ")
    else:
        for key in sql.keys():
            print(f"what {key} do you want in your query?")
            response = input("> ")
            sql[key] = response
        return
    return print(sql), print(sql_ready)
def execute_query():
    conn.execute(f"""{sql_ready}""")

if __name__ == "__main__":
    # collect_details(),
    collect_sql()
