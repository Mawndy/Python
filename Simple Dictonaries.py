# Simple Dictonaries

worker = {
    "name": "Steven Smith",
    "age": 30,
    "occupation": "Software Developer"
}

# Accessing dictionary values
print (worker["name"])

# Modifying dictionary values
worker["age"] = 31  
worker["occupation"] = "Senior Software Developer"

# Printing all key-value pairs
for key, value in worker.items():
    print(key, value)