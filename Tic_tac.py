# coding: utf-8
#CURRENCY CONVERTER
 
#list of currency symbols
s_currency=["0","XAF","ARS","AUD","BSD","BRL","BGN","CAD","CLP","CNY","COP","HRK","CYP","CZK","DKK","LTC","BTC","XCD","EEK","EUR","FJD","XPF","GHS","GTQ","HNL","HKD","HUF","ISK","INR","IDR","ILS","JMD","JPY","LVL","LTL","MYR","MXN","MAD","MMK","ANG","NZD","NOK","PKR","PAB","PEN","PHP","PLN","GOLD","QAR","RON","RUB","SAR","RSD","SGD","ZAR","KRW","LKR","SEK","CHF","TWD","THB","TTD","TND","TRY","AED","GBP","USD","VND","VEF"]
 
#list of currency values
s_curr_val=[0,582.43,14.32,1.30,1.0,3.74,1.73,1.2835,663.85,6.4825,2991.92,6.6401,0.519911,23.987,6.6060,0.3112,0.002376,2.6898,11.73,0.88,2.0501,105.90,3.8245,7.8792,22.550,7.7564,276.56,124.49,66.573,13232.29,3.7828,121.78,109.14,0.62,3.05,3.91,17.42,9.70,1178.2,1.79,1.45,8.24,104.67,1.0,3.27,46.14,3.82,0.000813,3.64,3.97,66.07,3.75,109.14,1.36,14.56,1151.75,146.25,8.14,0.97,32.41,35.11,6.60,2.02,2.85,3.67,0.71,1.0,22309.50,9.95,]
 
 
#taking user input for amount of UDS to convert then converting to int
firstCurrency=raw_input("How many US Dollars would you like to convert? Enter 0 to quit\n")
firstCurrency=float(firstCurrency)
print firstCurrency.__class__.__name__
 
if firstCurrency==0:
    print("Quitting program..")
    print firstCurrency.__class__.__name__
   
#Enter 0 and change the arg for s_currency to see where I left off....
    print(len(s_currency))
    print(len(s_curr_val))
    print(s_currency[1])
    print(s_curr_val[1])
 
elif firstCurrency!=0:
    #taking user inout for currency they want to convert USD into
    second_currency=raw_input("Enter Symbol of currency to convert USD into. Enter '0' to quit\n")
    print second_currency.__class__.__name__
 
    if second_currency=="0":
        print("Quitting program..")
        print second_currency.__class__.__name__
 
    elif second_currency==s_currency[1]:
        total=firstCurrency*s_curr_val[1]
        total=float(total)
        print second_currency.__class__.__name__
        print s_currency[1].__class__.__name__
        print s_curr_val[1].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
        print("You will get "+str(total)+" "+str(s_currency[1])+"'s for "+str(firstCurrency)+" US Dollars")
 
    elif second_currency==s_currency[2]:
        total=firstCurrency*s_curr_val[2]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[2])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[2].__class__.__name__
        print s_curr_val[2].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[3]:
        total=firstCurrency*s_curr_val[3]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[3])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[3].__class__.__name__
        print s_curr_val[3].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[4]:
        total=firstCurrency*s_curr_val[4]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[4])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[4].__class__.__name__
        print s_curr_val[4].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[5]:
        total=firstCurrency*s_curr_val[5]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[5])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[5].__class__.__name__
        print s_curr_val[5].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[6]:
        total=firstCurrency*s_curr_val[6]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[6])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[6].__class__.__name__
        print s_curr_val[6].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[7]:
        total=firstCurrency*s_curr_val[7]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[7])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[7].__class__.__name__
        print s_curr_val[7].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[8]:
        total=firstCurrency*s_curr_val[8]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[8])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[8].__class__.__name__
        print s_curr_val[8].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[9]:
        total=firstCurrency*s_curr_val[9]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[9])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[9].__class__.__name__
        print s_curr_val[9].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[10]:
        total=firstCurrency*s_curr_val[10]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[10])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[10].__class__.__name__
        print s_curr_val[10].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[11]:
        total=firstCurrency*s_curr_val[11]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[11])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[11].__class__.__name__
        print s_curr_val[11].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[12]:
        total=firstCurrency*s_curr_val[12]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[12])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[12].__class__.__name__
        print s_curr_val[12].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[13]:
        total=firstCurrency*s_curr_val[13]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[13])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[13].__class__.__name__
        print s_curr_val[13].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[14]:
        total=firstCurrency*s_curr_val[14]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[14])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[14].__class__.__name__
        print s_curr_val[14].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[15]:
        total=firstCurrency*s_curr_val[15]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[15])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[15].__class__.__name__
        print s_curr_val[15].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[16]:
        total=firstCurrency*s_curr_val[16]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[16])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[16].__class__.__name__
        print s_curr_val[16].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[17]:
        total=firstCurrency*s_curr_val[17]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[17])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[17].__class__.__name__
        print s_curr_val[17].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[18]:
        total=firstCurrency*s_curr_val[18]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[18])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[18].__class__.__name__
        print s_curr_val[18].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[19]:
        total=firstCurrency*s_curr_val[19]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[19])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[19].__class__.__name__
        print s_curr_val[19].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[20]:
        total=firstCurrency*s_curr_val[20]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[20])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[20].__class__.__name__
        print s_curr_val[20].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[21]:
        total=firstCurrency*s_curr_val[21]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[21])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[21].__class__.__name__
        print s_curr_val[21].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[22]:
        total=firstCurrency*s_curr_val[22]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[22])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[22].__class__.__name__
        print s_curr_val[22].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[23]:
        total=firstCurrency*s_curr_val[23]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[23])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[23].__class__.__name__
        print s_curr_val[23].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[24]:
        total=firstCurrency*s_curr_val[24]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[24])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[24].__class__.__name__
        print s_curr_val[24].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[25]:
        total=firstCurrency*s_curr_val[3]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[25])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[25].__class__.__name__
        print s_curr_val[25].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[26]:
        total=firstCurrency*s_curr_val[26]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[26])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[26].__class__.__name__
        print s_curr_val[26].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[27]:
        total=firstCurrency*s_curr_val[27]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[27])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[27].__class__.__name__
        print s_curr_val[27].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[28]:
        total=firstCurrency*s_curr_val[28]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[28])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[28].__class__.__name__
        print s_curr_val[28].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[29]:
        total=firstCurrency*s_curr_val[29]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[29])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[29].__class__.__name__
        print s_curr_val[29].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[30]:
        total=firstCurrency*s_curr_val[30]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[30])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[30].__class__.__name__
        print s_curr_val[30].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[31]:
        total=firstCurrency*s_curr_val[31]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[31])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[31].__class__.__name__
        print s_curr_val[31].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[32]:
        total=firstCurrency*s_curr_val[32]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[32])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[32].__class__.__name__
        print s_curr_val[32].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[33]:
        total=firstCurrency*s_curr_val[33]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[33])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[33].__class__.__name__
        print s_curr_val[33].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[34]:
        total=firstCurrency*s_curr_val[34]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[34])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[34].__class__.__name__
        print s_curr_val[34].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[35]:
        total=firstCurrency*s_curr_val[35]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[35])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[35].__class__.__name__
        print s_curr_val[35].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[36]:
        total=firstCurrency*s_curr_val[36]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[36])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[36].__class__.__name__
        print s_curr_val[36].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[37]:
        total=firstCurrency*s_curr_val[37]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[37])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[37].__class__.__name__
        print s_curr_val[37].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[37]:
        total=firstCurrency*s_curr_val[37]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[37])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[37].__class__.__name__
        print s_curr_val[37].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[38]:
        total=firstCurrency*s_curr_val[38]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[38])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[38].__class__.__name__
        print s_curr_val[38].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[39]:
        total=firstCurrency*s_curr_val[39]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[39])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[39].__class__.__name__
        print s_curr_val[39].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[40]:
        total=firstCurrency*s_curr_val[40]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[40])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[40].__class__.__name__
        print s_curr_val[40].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[41]:
        total=firstCurrency*s_curr_val[41]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[41])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[41].__class__.__name__
        print s_curr_val[41].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[42]:
        total=firstCurrency*s_curr_val[42]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[42])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[42].__class__.__name__
        print s_curr_val[42].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[43]:
        total=firstCurrency*s_curr_val[43]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[43])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[43].__class__.__name__
        print s_curr_val[43].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[44]:
        total=firstCurrency*s_curr_val[44]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[44])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[44].__class__.__name__
        print s_curr_val[44].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[45]:
        total=firstCurrency*s_curr_val[45]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[45])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[45].__class__.__name__
        print s_curr_val[45].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[46]:
        total=firstCurrency*s_curr_val[46]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[46])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[46].__class__.__name__
        print s_curr_val[46].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[47]:
        total=firstCurrency*s_curr_val[47]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[47])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[47].__class__.__name__
        print s_curr_val[47].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[48]:
        total=firstCurrency*s_curr_val[48]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[48])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[48].__class__.__name__
        print s_curr_val[48].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[49]:
        total=firstCurrency*s_curr_val[49]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[49])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[49].__class__.__name__
        print s_curr_val[49].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[50]:
        total=firstCurrency*s_curr_val[50]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[50])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[50].__class__.__name__
        print s_curr_val[50].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[51]:
        total=firstCurrency*s_curr_val[51]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[51])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[51].__class__.__name__
        print s_curr_val[51].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[52]:
        total=firstCurrency*s_curr_val[52]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[52])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[52].__class__.__name__
        print s_curr_val[52].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[53]:
        total=firstCurrency*s_curr_val[53]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[54])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[54].__class__.__name__
        print s_curr_val[54].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[55]:
        total=firstCurrency*s_curr_val[55]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[55])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[55].__class__.__name__
        print s_curr_val[55].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[56]:
        total=firstCurrency*s_curr_val[56]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[56])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[56].__class__.__name__
        print s_curr_val[56].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[57]:
        total=firstCurrency*s_curr_val[57]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[57])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[57].__class__.__name__
        print s_curr_val[57].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[58]:
        total=firstCurrency*s_curr_val[58]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[58])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[58].__class__.__name__
        print s_curr_val[58].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[58]:
        total=firstCurrency*s_curr_val[58]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[58])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[58].__class__.__name__
        print s_curr_val[58].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[59]:
        total=firstCurrency*s_curr_val[59]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[59])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[59].__class__.__name__
        print s_curr_val[59].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[60]:
        total=firstCurrency*s_curr_val[60]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[60])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[60].__class__.__name__
        print s_curr_val[60].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[61]:
        total=firstCurrency*s_curr_val[61]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[61])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[61].__class__.__name__
        print s_curr_val[61].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[61]:
        total=firstCurrency*s_curr_val[61]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[61])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[61].__class__.__name__
        print s_curr_val[61].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[62]:
        total=firstCurrency*s_curr_val[62]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[62])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[62].__class__.__name__
        print s_curr_val[62].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[63]:
        total=firstCurrency*s_curr_val[63]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[63])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[63].__class__.__name__
        print s_curr_val[63].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[64]:
        total=firstCurrency*s_curr_val[64]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[64])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[64].__class__.__name__
        print s_curr_val[64].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[65]:
        total=firstCurrency*s_curr_val[65]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[65])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[65].__class__.__name__
        print s_curr_val[65].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[66]:
        total=firstCurrency*s_curr_val[66]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[66])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[66].__class__.__name__
        print s_curr_val[66].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[67]:
        total=firstCurrency*s_curr_val[67]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[67])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[67].__class__.__name__
        print s_curr_val[67].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[68]:
        total=firstCurrency*s_curr_val[68]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[68])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[68].__class__.__name__
        print s_curr_val[68].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    elif second_currency==s_currency[69]:
        total=firstCurrency*s_curr_val[69]
        total=float(total)
       
        print("You will get "+str(total)+" "+str(s_currency[69])+"'s for "+str(firstCurrency)+" US Dollars")
        print second_currency.__class__.__name__
        print s_currency[69].__class__.__name__
        print s_curr_val[69].__class__.__name__
        print firstCurrency.__class__.__name__
        print total.__class__.__name__
       
    else:
        print("Invalid input.. you suck..")
 
else:
    print("Please enter a valid Unit Name or Symbol or enter 'Quit' to quit")
    print("This is the closing Else statement that is displaying...")
    print firstCurrency.__class__.__name__
    print  s_currency.__class__.__name__
