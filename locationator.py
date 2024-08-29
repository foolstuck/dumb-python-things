import ipinfo
import tkinter as tk
import phonenumbers, pycountry
from phonenumbers.phonenumberutil import region_code_for_number

def display_info(self):
    txt = inputbox.get()
    if '.' in txt or ':' in txt:
        try:
            token = 'cde05570050a71'
            handler = ipinfo.getHandler(token)
            details = handler.getDetails(txt)
            dis.config(text = details.city + ', ' + details.country)
        except:
            dis.config(text = '玩呢？')
    else:
        try:
            if '+' in txt:
                numba = phonenumbers.parse(txt)
                country = pycountry.countries.get(alpha_2 = region_code_for_number(numba))
                dis.config(text = country.name)
            else:
                txt = '+' + txt
                numba = phonenumbers.parse(txt)
                country = pycountry.countries.get(alpha_2 = region_code_for_number(numba))
                dis.config(text = country.name)
        except:
            dis.config(text = '你这是正经电话，我吃屎！')

window = tk.Tk()
window.eval('tk::PlaceWindow . center')
window.title("Locationator")
window.geometry('250x180')

window.resizable(width=False, height=False)
txt = tk.Label(text = '请输入区号或 IP 地址')
txt.pack(pady=20)
inputbox = tk.Entry(window)
inputbox.pack()
dis = tk.Label()
dis.pack(pady=20)
window.bind('<Return>', display_info)
window.mainloop()

# if '.' in input or ':' in input: 
#     try:
#         info = handler.getDetails(input)
#         info = info.country + ', ' + info.city
#     except:
#         info = "玩呢？"
# else:
#     print('电话')