#List of available cars and their prices
cars={
   
      "2023 Mercedes-Benz G-Class":139900,
      "2023 Mercedes-Benz GLA-Class":37500,
      "2023 Mercedes-Benz GLS-Class":81800,
      "2023 Mercedes-Benz S-Class":114500,
      "2022 Mercedes-Benz A-Class":33950,
      "2011 Ferrari California":42445,
      "2010 Ferrari California":45446,
      "2010 Ferrari F458 Italia":115366,
      "2009 Ferrari 599 GTB Fiorano":89609,
      "2008 Ferrari 612 Scaglietti":44374,
      "2008 Ferrari F430":46173,
      "2023 Chevrolet Blazer":35100,
      "2023 Chevrolet Bolt":25600,
      "2023 Chevrolet Camaro":26400,
      "2023 Chevrolet Malibu":25000,
      "2023 Chevrolet Silverado 1500":35600,
      "2023 Chevrolet Traverse":34520,
      "2009 Hummer H2":28592,
      "2009 HUMMER H2 SUT":29101,
      "2009 Hummer H3":10372,
      "2009 HUMMER H3T":14960,
      "2008 Hummer H2":20823,
      "2007 Hummer H2":15302,
      "2023 GMC Terrain":29900,
      "2022 Porsche 911":78900,}
#get user input for car name
car_name = input("Enter a car_name: ")
#check if car is in the list of available cars
if car_name in cars:
    print("Yes")
    #if car name is present, get its list
    car_price=cars[car_name]
    print(f"The price of {car_name} is {car_price}.")
else:
    #if car name is not present, inform the user
    print(f"sorry,{car_name} is not available.")
https://github.com/Opareosman/Data-Structure
