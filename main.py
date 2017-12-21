import sys
import os
from lib.notification import sendmail
#from lib.scale import Scale, Product
from lib.read_serial import getSerial
import pandas as pd


if __name__ == '__main__':
	df = pd.read_csv('sample.csv')         #Opens the database as a dataframe
	"""id = 49
	name, product_cat, quantity = df["Product Name"][id], df["Product Sub-Category"][id], df["Order Quantity"][id]
	scale = Scale('abc', Product(name, product_cat,quantity, 50, 90))
	print(scale.product.name)"""
	for i in range(5):                     #This loop is for how many times you want to get data from each of the load cells. For future use convert this to a while loop so that it runs continuously indefinitely
                pairs = getSerial()        #This calls the function getSerial() which returns a dictionary containing load cell/arduino ids as keys and weights measured by them as the respective values
                #print(diction)
                #print(df)
                for k,v in pairs.iteritems():                         #looping over the key value pairs
                        for i in range(df.shape[0]):				  #To loop over the rows. In future use iterrows()
                                if str(k) == str(df["ID"][i]):        #To make sure that the id in the dataframe matches the id in pairs
                                        df["W"][i] = v #W is the current weight  #Update the weight in the dataframe with the new weight measured

                for i in range(df.shape[0]):                          #Looping over rows of dataframe
                        print( df['W'][i] , df['Product'][i])  		  #Print weight of product and product name
                        if((float(df['W'][i]) < float(df['InitW'][i]) * int(df['minL'][i])/100) and df['S'][i] == 0):  #If weight falls below threshold and a mail hasn't been sent already for the materal
                                sendmail(df['Product'][i], df['jsno'][i])   										   #Send notification via email by calling function sendmail()
                                df['S'][i] = 1							#Update the database to make sure that an email for the product replenishment has been sent
                df.to_csv('sample.csv', index = False)					#Save the new updated dataframe by overwriting the original csv file

