#import json
import requests
import json
import glob
import time

def get_dataset_from_vip():
    url = 'https://indodax.com/api/btc_idr/trades'
    data = requests.get(url)
    data = data.json()
    print('trades data saved')
    save_to_csv(data,"trades")
    
    url = 'https://indodax.com/api/btc_idr/depth'
    data = requests.get(url)
    data = data.json()
    print('depth data saved')
    save_to_csv(data,"depth")    
    
def save_to_csv(data,folder):
    total_doc = len(glob.glob('./dataset/'+str(folder)+'/*'))
    filename = './dataset/'+str(folder)+'/'+str(folder)+'_'+str(total_doc)+'.json'
    with open(filename, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

while True:
    get_dataset_from_vip()
    time.sleep(5)