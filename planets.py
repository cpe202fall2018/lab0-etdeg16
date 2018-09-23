#
#Name; Ethan De Guzman
#Student ID: 012820349
#Date (last modified): 9/22/2018
#
#Lab 0
#Section 16
#Purpose of lab: To get comfortable programming in a Python enivornment and with testing.

def weight_on_planets():
    earth_weight = float(input("What do you weigh on earth? "))
    mars_weight = earth_weight * 0.38
    jupiter_weight = earth_weight * 2.34
    print ("\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds.".format(mars_weight, jupiter_weight))
   
   
   
if __name__ == '__main__':
    weight_on_planets()
