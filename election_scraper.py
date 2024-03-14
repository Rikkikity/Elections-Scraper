"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jiří Albrecht

email: albrecht1994@seznam.cz

discord: Rikkiti#3029

"""

from requests import get
from bs4 import BeautifulSoup
import csv
import sys

# extract data from url and parse them
def data_parserer(url:str) -> 'bs4.BeautifulSoup': 
    url_data = get(url)
    data_parser = BeautifulSoup(url_data.text, features="html.parser")
    return data_parser

def dict_sum (dict_name:dict,key:str,value:str) -> None:
    if key in dict_name:
        dict_name[key] = str(int(dict_name[key])+int(value))
    else:
        dict_name[key] = value

def join_adress(start:str,finish:str) -> str:
    adress = [start, finish]
    full_adress = "/".join(adress)
    return full_adress 

# validation of input arguments
if len(sys.argv) != 3:
    print(
        "The 'address' or 'name of the resulting file' argument is missing for launch",
    )
    print("The program will exit, please run the program with two input arguments")
    exit()
else:
    print(f"Downloading data at the selected URL:{sys.argv[1]}")

main_url = sys.argv[1]

core_url = "/".join((main_url.split("/"))[0:-1])

main_url_parsered = data_parserer(main_url)
# list of villages
table_village = main_url_parsered.find_all("tr")

# main data dict
data_sheet = {}

for village in table_village:
    
    sheet = {}
    try:
        sheet["Code"] = village.find_all("td")[0].text
        sheet["Location"] = village.find_all("td")[1].text
        sub_url = village.find_all("td")[2]("a")[0].attrs["href"]

        # link to subpage
        full_adress = join_adress(core_url,sub_url)   
        
        # checking if secondary subpages exist
        adress_test = data_parserer(full_adress)
        test_multiple_url = adress_test.find_all("td",{"headers":"s1"})
        
        # list of subadress
        sub_url_list = []      
        if len(test_multiple_url) !=0:
            for link in test_multiple_url:
                sub_url_list.append(link.find_all("a")[0].attrs["href"])
        else:
            sub_url_list=[sub_url]
        
        # browsing sub-addresses
        for link in sub_url_list:
            adress = [core_url, link]
            full_adress = ("/".join(adress))   
            subadress_parsered = data_parserer(full_adress)
            # voters in the list
            dict_sum(sheet,"Registred", subadress_parsered.find("td",{"headers":"sa2"}).text.replace("\xa0",""))
            
            # issued envelopes
            dict_sum(sheet,"Envelopes", subadress_parsered.find("td",{"headers":"sa5"}).text.replace("\xa0",""))

            # valid votes
            dict_sum(sheet,"Valid", subadress_parsered.find("td",{"headers":"sa6"}).text.replace("\xa0",""))

            all_parties = subadress_parsered.find_all("tr")

            # elected parties extractor
            # 5 to skip headings and -1 to cut off the empty last line
            for village in all_parties[5:-1]:
                try:
                    dict_sum(sheet,village.findAll("td")[1].text,village.findAll("td")[2].text.replace("\xa0",""))
                
                except IndexError:
                    pass 
        # inserting data into the dictionary under the name of the village
        data_sheet[sheet["Location"]] = sheet   
    
    except IndexError:
        pass


# csv generator
print(f"I am creating a CSV file named: {sys.argv[2]}")
new_csv = open(sys.argv[2], mode="w") 
csv_writer = csv.writer(new_csv)


head = next(iter(data_sheet.values())).keys()
csv_writer.writerow(head)

for village in data_sheet:
    csv_data = data_sheet[village].values()
    csv_writer.writerow(csv_data)

new_csv.close()
