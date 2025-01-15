import pandas as pd
import matplotlib.pyplot as plt

# Sample rent data (use actual data here)
data = {
    "Location": ["Ajegunle (Ikorodu)", "Ajegunle (Ikorodu)", "Ajegunle (Ikorodu)", "Ajegunle (Ikorodu)", "Ajegunle (Ikorodu)",
                 "Mile12", "Mile12", "Mile12", "Mile12", "Mile12",
                 "Ketu", "Ketu", "Ketu", "Ketu", "Ketu",
                 "Ikeja", "Ikeja", "Ikeja", "Ikeja", "Ikeja"],
    "Unit_Type": ["Single Room", "Self Contained", "Mini-Flat", "2 Bedroom", "3 Bedroom",
                  "Single Room", "Self Contained", "Mini-Flat", "2 Bedroom", "3 Bedroom",
                  "Single Room", "Self Contained", "Mini-Flat", "2 Bedroom", "3 Bedroom",
                  "Single Room", "Self Contained", "Mini-Flat", "2 Bedroom", "3 Bedroom"],
    "Rent": [15000, 25000, 40000, 60000, 80000, 20000, 30000, 50000, 70000, 100000, 18000, 27000, 45000, 65000, 85000, 22000, 32000, 55000, 75000, 110000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate average rent for each location and unit type
avg_rent = df.groupby(["Location", "Unit_Type"])["Rent"].mean().unstack()

# Plotting the data
avg_rent.plot(kind='bar', figsize=(10, 6), colormap='viridis')
plt.title("Average Rent by Location and Unit Type")
plt.ylabel("Average Rent (NGN)")
plt.xlabel("Location")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
