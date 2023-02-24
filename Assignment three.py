#list of cars and their prices
print('Welcome to Crella cars garage')
carBrand={'Scion':'$600',
          'Bugatti':'$890',
          'Lincoln':'$790',
          'Alfa Romeo':'$765',
          'Ram Trucks':'$987',
          'Pontiac':'$887',
          'Fiat':'$780',
          'Nissan':'$50',
          'Chevrolet':'$80',
          'Porche':'$456',
          'Ford':'$149',
          'Acura':'$110,900',
          'Volvo':'$23,400',
          'Kia':'$23,000',
          'Volkswagen':'$650',
          'Toyota':'$230',
          'Madza':'$130',
          'Jaguar':'$768',
          'Lexus':'$665',
          'Mini':'112',
          'Tesla':'$336',
          'Jeep':'998',
          'Subaru':'$887',
          'Mercedes-Benz':'334',
          'Honda':'$900',
          'Mitsubishi':'776',
          'Buick':'$876',
          'GMC':'$566'}
carName=input('input car of choice:').strip()
#check if carBrand in carName
if carName in carBrand:
    print(' carBrand available')
#if carName in carBrand is available, get its price
carPrice=carBrand[carName]
print(f'The price of {carName} is ${carPrice}.')