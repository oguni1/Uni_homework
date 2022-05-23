import pandas as pd
import matplotlib.pyplot as plt

Laptop_Data = pd.read_csv('Cleaned_Laptop_data.csv')
print(Laptop_Data.to_string())

Intel_proc_count = 0
AMD_proc_count = 0
for i in range(len(Laptop_Data.index)):
    if Laptop_Data.iloc[i]['processor_brand'] == 'Intel':
        Intel_proc_count += 1
    if Laptop_Data.iloc[i]['processor_brand'] == 'AMD':
        AMD_proc_count += 1
group = ['Intel', 'AMD']
both_proc = [Intel_proc_count, AMD_proc_count]
plt.title('Общее количество процессоров')
plt.bar(group, both_proc)
plt.show()

Intel_gnrtions = []
AMD_gnrtions = []
for i in range(len(Laptop_Data.index)):
    if Laptop_Data.iloc[i]['processor_brand'] == 'Intel':
        if not Intel_gnrtions.__contains__(Laptop_Data.iloc[i]['processor_gnrtn']):
            Intel_gnrtions.append(Laptop_Data.iloc[i]['processor_gnrtn'])
    if Laptop_Data.iloc[i]['processor_brand'] == 'AMD':
        if not AMD_gnrtions.__contains__(Laptop_Data.iloc[i]['processor_gnrtn']):
            AMD_gnrtions.append(Laptop_Data.iloc[i]['processor_gnrtn'])

both_proc_gen = [len(Intel_gnrtions), len(AMD_gnrtions)]
plt.title('Общее количество поколений процессоров')
plt.bar(group, both_proc_gen)
plt.show()