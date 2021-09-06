countries_file = open('countries.txt','r');
print(countries_file.readlines());
for files in countries_file.readlines():
    print(files);
countries_file.close();