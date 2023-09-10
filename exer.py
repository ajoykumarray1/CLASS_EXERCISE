county_list = [1,2,3,4,5,6,7,8,9,10,11]

county = input("Enter Country name: ")

index = int(input(f"Please enter index number between 0 and {len(county_list) - 1} to add country: "))

county_list.insert(index, county)
print(county_list)