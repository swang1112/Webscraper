from datetime import datetime
import pandas as pd
import requests


def main():
    my_url = "https://api.alternative.me/fng/?limit=0" 
    response = requests.get(my_url)
    print(response.status_code)

    my_data = response.json()["data"]

    date = []
    value = []
    for i in my_data:
        date_temp = datetime.utcfromtimestamp(int(i["timestamp"])).strftime('%Y-%m-%d')
        date.append(date_temp)
        value.append(i["value"])

    output = {"date": date, "value": value}
    output_df = pd.DataFrame(output)

    return output_df

if __name__ == "__main__":
    df = main()
    df.to_csv(file_name, header=True)