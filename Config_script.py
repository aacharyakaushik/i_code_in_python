# import pandas as pd

# path = "C:/Users/Kaushik Acharya/Documents/lat_long_list.csv"

# df = pd.read_csv(path)
# df["Model"] = "bcc-csm1-1"
# df["Scenario"] = "rcp45"

# df.to_csv("C:/Users/Kaushik Acharya/Documents/New folder/1.csv", sep=',', index = False)


for i in range(12,58):
    with open("C:/Users/Kaushik Acharya/Documents/New folder/" + str(i) + ".csv",'r') as f:
        with open("C:/Users/Kaushik Acharya/Documents/New folder2/" + str(i) + ".csv",'w') as f1:
            next(f) # skip header line
            for line in f:
                f1.write(line)
# import os
# csv_header = 'Locations, Model, Scenarios'
# csv_out = 'consolidated_Config.csv'
# csv_dir = 'C:/Users/Kaushik Acharya/Documents/New folder/'

# dir_tree = os.walk(csv_dir)
# for dirpath, dirnames, filenames in dir_tree:
#    pass

# csv_list = []
# for file in filenames:
#    if file.endswith('.csv'):
#       csv_list.append(file)

# csv_merge = open(csv_out, 'w')
# csv_merge.write(csv_header)
# csv_merge.write('\n')

# for file in csv_list:
#    csv_in = open(file)
#    for line in csv_in:
#       if line.startswith(csv_header):
#          continue
#       csv_merge.write(line)
#    csv_in.close()
#    csv_merge.close()
# print('Verify consolidated CSV file : ' + csv_out)