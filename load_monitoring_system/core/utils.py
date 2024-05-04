import json
import gspread
import requests


gc = gspread.service_account(filename=r"core\creds\vast-tributary-416405-83f965d6e4a2.json")
sh = gc.open("Data logging system")

def retrieve(*header):
    
    # gc = gspread.service_account(filename=r"C:\Users\djaha\Documents\GithubProjects\Unuploaded\gspread-test\vast-tributary-416405-83f965d6e4a2.json")

    headers = ['Date', 'Time', 'Voltage A', 'Voltage B', 'Voltage C', 'Current A', 'Current B', 'Current C', 'Apparent Power A (kva)', 'Apparent Power B (kva)', 'Apparent Power C (kva)', 'Percent Transformer Load (PTL)', 'Percent Voltage Imbalance (PVI)', 'Percen Current Imbalance (PCI)']

    # sh = gc.open("Gspread-test")

    worksheet_transformer = sh.get_worksheet(1)

    datas = worksheet_transformer.get_all_records()
    
    def get_data_from_header(data, header=header, additional_params=True):      
        arr = []
        
        colors_primary = ["red", "blue", "green", "yellow", "brown", "black", "orange"]
        colors_darker = [
                "rgb(128, 0, 0)",    # Red
                "rgb(0, 128, 0)",    # Green
                "rgb(0, 0, 128)",    # Blue
                "rgb(128, 128, 0)",  # Yellow
                "rgb(128, 0, 128)",  # Magenta
                "rgb(0, 128, 128)",  # Cyan
                "rgb(64, 0, 0)",     # Dark Red
                "rgb(0, 64, 0)",     # Dark Green
                "rgb(0, 0, 64)",     # Dark Blue
                "rgb(64, 64, 64)"    # Gray
            ]
        
        colors_lighter = [
                "rgb(128, 0, 0)",     # Darker shade of Red
                "rgb(255, 128, 128)", # Lighter shade of Red
                "rgb(0, 128, 0)",     # Darker shade of Green
                "rgb(128, 255, 128)", # Lighter shade of Green
                "rgb(0, 0, 128)",     # Darker shade of Blue
                "rgb(128, 128, 255)", # Lighter shade of Blue
                "rgb(128, 128, 0)",   # Darker shade of Yellow
                "rgb(255, 255, 128)", # Lighter shade of Yellow
                "rgb(128, 0, 128)",   # Darker shade of Magenta
                "rgb(255, 128, 255)", # Lighter shade of Magenta
                "rgb(0, 128, 128)",   # Darker shade of Cyan
                "rgb(128, 255, 255)", # Lighter shade of Cyan
                "rgb(64, 0, 0)",      # Darker shade of Dark Red
                "rgb(128, 64, 64)",   # Lighter shade of Dark Red
                "rgb(0, 64, 0)",      # Darker shade of Dark Green
                "rgb(64, 128, 64)",   # Lighter shade of Dark Green
                "rgb(0, 0, 64)",      # Darker shade of Dark Blue
                "rgb(64, 64, 128)",   # Lighter shade of Dark Blue
                "rgb(64, 64, 64)",    # Darker shade of Gray
                "rgb(192, 192, 192)"  # Lighter shade of Gray
            ]


        for h in header:
            if additional_params:
                json_data = {}
                json_data['label'] = h
                json_data['data'] = [d[h] for d in data if h in data[0].keys()]
                json_data['borderColor'] = colors_primary[header.index(h)]
                json_data['fill'] = False
                arr.append(json.dumps(json_data))
            else:
                arr = [d[h] for d in data if h in data[0].keys()]
            
            
        return arr
       
        
    jsoned = {}
    jsoned["datasets"] = get_data_from_header(data=datas)
    jsoned["labels"] = get_data_from_header(data=datas, header=['Time'],additional_params=False)
    

    return jsoned


def retrieve_all_data():
    # gc = gspread.service_account(filename=r"core\creds\vast-tributary-416405-83f965d6e4a2.json")
    # sh = gc.open("Data logging system")
    
    headers = ['Date', 'Time', 'VoltageA', 'VoltageB', 'VoltageC', 'CurrentA', 'CurrentB', 'CurrentC', 'Apparent Power A (kva)', 'Apparent Power B (kva)', 'Apparent Power C (kva)', 'Percent Transformer Load (PTL)', 'Percent Voltage Imbalance (PVI)', 'Percen Current Imbalance (PCI)']
    data = {}
    # gc = gspread.service_account(filename=r"C:\Users\djaha\Documents\GithubProjects\Unuploaded\gspread-test\vast-tributary-416405-83f965d6e4a2.json")

    # sh = gc.open("Gspread-test")

    worksheet_transformer = sh.get_worksheet(1)

    datas = worksheet_transformer.get_all_records()

    headers = datas[0].keys()

    
    for header in headers:
        try:
            data[header] = [datas[n][header] for n in range(len(datas))]
        except Exception:
            print("Error: ", Exception)

    
    return data

retrieve_all_data()





