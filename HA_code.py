import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

URL = "https://www.landesmuseum-stuttgart.de/lmwallobjects.json"



# Fetch JSON data from a given url
df = pd.read_json(URL, orient="columns")

# View the first ten rows
new_df = df.head(10)
# print(new_df)

### plot the received data ###

# create a subplot
fig, ax = plt.subplots()

# drop not available (na) data
df_cleaned = new_df.dropna(how='all')

name = df_cleaned["objekt_name"]
id = df_cleaned["objekt_id"]

jahreszahlen = []
for element in name:
    object_year = element[-4:]
    print(object_year)
    jahreszahlen.append(object_year)
print(jahreszahlen)

objektnamen = []
for item in name:
    object_name = item[0:-5]
    for thing in id:
        object_id = thing
        important_info = str(object_name + " " + str(object_id))
        objektnamen.append(important_info)
print(objektnamen)

# x = df_cleaned["objekt_id"].values
# y = df_cleaned["objekt_erfasst_am"].values
#
# plt.title("Test", size="x-large")
# plt.ylabel("erfasst am", size="x-large")
# plt.xlabel("ObjektID", size="x-large")
#
# plt.plot(y, "*-", markersize=6, linewidth=1, color="r")
#
# plt.legend(loc=(0.4, 0.2))
#
# ax.set_xticks(range(len(x)))
# ax.set_xticklabels(x, rotation="vertical")
#
# plt.show()


