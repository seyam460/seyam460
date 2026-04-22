import pandas as pd 


data = {
    "name": ["john", "doe", "jane", "smith"],
    "age" : ["30", "25", "28", "35"],
    "gender" : ["male", "female", "female", "male"]

}

df = pd.DataFrame(data)

print(df)

