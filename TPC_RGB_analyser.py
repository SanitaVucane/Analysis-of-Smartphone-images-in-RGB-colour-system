import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Title and name of the algorithm version
print("Analysis of smartphone images in the RGB color system")
print("Algorithm version: v.1.0")
print()

# Prompt the user to enter a unit of measure
unit = input("Please enter concentration unit (eg mg L-1): ")

# Prompt user for I0 value
I0 = int(input("Please enter the I0 value of the Comparison solution:"))

# Prompt the user to enter the number of calibration solution points
n_points = int(input("Please enter the number of calibration solution points:"))

# Create empty lists for concentrations and RGB values concentrations
concentrations = []
R = []
G = []
B = []

# Prompt the user for each concentration value, R, G and B values
for i in range(1, n_points+1):
    concentration = float(input(f"Please enter the value of concentration {i} ({unit}):"))
    concentrations.append(concentration)

    r = int(input(f"Please enter the {concentration} {unit} R value:"))
    g = int(input(f"Please enter the value of concentration {concentration} {unit} G value"))
    b = int(input(f"Please enter the value of concentration {concentration} {unit} B value  "))
    R.append(r)
    G.append(g)
    B.append(b)

# Convert lists to NumPy arrays
concentrations = np.array(concentrations)
R = np.array(R)
G = np.array(G)
B = np.array(B)

# Calculation of absorption
A_R = -np.log(R / I0)
A_G = -np.log(G / I0)
A_B = -np.log(B / I0)

print(f"Concentration ({unit}): {concentrations}")
print(f"Absorption R {A_R}")
print(f"Absorption G {A_G}")
print(f"Absorption B {A_B}")

# Calculate combined channel absorptions
A_RGB = (A_R + A_G + A_B) / 3
A_RG = (A_R + A_G) / 2
A_RB = (A_R + A_B) / 2
A_GB = (A_G + A_B) / 2

def linear_regression(x, y):
    slope, intercept, r_value, _, _ = linregress(x, y)
    R2 = r_value**2
    equation = f"y = {slope:.2f}x + {intercept:.4f}"
    return slope, intercept, R2, equation

slope_R, intercept_R, R2_R, _ = linear_regression(concentrations, A_R)
slope_G, intercept_G, R2_G, _ = linear_regression(concentrations, A_G)
slope_B, intercept_B, R2_B, _ = linear_regression(concentrations, A_B)
slope_RGB, intercept_RGB, R2_RGB, _ = linear_regression(concentrations, A_RGB)
slope_RG, intercept_RG, R2_RG, _ = linear_regression(concentrations, A_RG)
slope_RB, intercept_RB, R2_RB, _ = linear_regression(concentrations, A_RB)
slope_GB, intercept_GB, R2_GB, _ = linear_regression(concentrations, A_GB)

# Drawing calibration curves
plt.figure(figsize=(12, 8))

def plot_calibration_curve(x, y, slope, intercept, R2, label, color):
    plt.scatter(x, y, color=color, label=f'{label} channel')
    plt.plot(x, slope * x + intercept, color=color, linewidth=2)
    plt.xlabel(f'Concentration ({unit})')
    plt.ylabel('Absorption')
    plt.legend()

# Draw the calibration curve for each color channel
plot_calibration_curve(concentrations, A_R, slope_R, intercept_R, R2_R, 'R', 'red')
plot_calibration_curve(concentrations, A_G, slope_G, intercept_G, R2_G, 'G', 'green')
plot_calibration_curve(concentrations, A_B, slope_B, intercept_B, R2_B, 'B', 'blue')
plot_calibration_curve(concentrations, A_RGB, slope_RGB, intercept_RGB, R2_RGB, 'RGB', 'purple')
plot_calibration_curve(concentrations, A_RG, slope_RG, intercept_RG, R2_RG, 'RG', 'orange')
plot_calibration_curve(concentrations, A_RB, slope_RB, intercept_RB, R2_RB, 'RB', 'cyan')
plot_calibration_curve(concentrations, A_GB, slope_GB, intercept_GB, R2_GB, 'GB', 'magenta')

# Set graphics name and display graphics
plt.title('Calibration curves for R, G, B, RGB, RG, RB and GB color channels')
plt.show()

# Create a data structure with R² values and equations
data = {
    "Channel": ["R", "G", "B", "RGB", "RG", "RB", "GB"],
    "R²": [R2_R, R2_G, R2_B, R2_RGB, R2_RG, R2_RB, R2_GB],
    "Equation": [f"y = {slope_R:.4f}x + {intercept_R:.4f}",
                    f"y = {slope_G:.4f}x + {intercept_G:.4f}",
                    f"y = {slope_B:.4f}x + {intercept_B:.4f}",
                    f"y = {slope_RGB:.4f}x + {intercept_RGB:.4f}",
                    f"y = {slope_RG:.4f}x + {intercept_RG:.4f}",
                    f"y = {slope_RB:.4f}x + {intercept_RB:.4f}",
                    f"y = {slope_GB:.4f}x + {intercept_GB:.4f}"]
}

# Create a pandas DataFrame with R² values
R2_df = pd.DataFrame(data)

# Printing the DataFrame
print(R2_df)

# Ask the user to enter the number of samples to be analyzed
n_unknown_samples = int(input("Please enter the number of samples to analyze:"))

# Choose which channels to calculate the concentration
channels = input("Please select a channel to calculate concentration (R, G, B, RGB, RG, RB, GB)")

# Getting analyzed sample names
unknown_sample_names = []
for i in range(1, n_unknown_samples + 1):
    sample_name = input(f"Please enter the name of the sample {i} to be analyzed")
    unknown_sample_names.append(sample_name)

# Obtaining the values of the analyzed samples and calculating the concentration
unknown_concentrations = []

for i in range(n_unknown_samples):
    if channels == "R":
        r = int(input(f"Please enter the R value of the sample to be analyzed {unknown_sample_names[i]}:"))
        A = -np.log(r / I0)
        concentration = (A - intercept_R) / slope_R
    elif channels == "G":
        g = int(input(f"Please enter the G value of the sample to be analyzed {unknown_sample_names[i]}:  "))
        A = -np.log(g / I0)
        concentration = (A - intercept_G) / slope_G
    elif channels == "B":
        b = int(input(f"Please enter the B value of the sample to be analyzed {unknown_sample_names[i]}: "))
        A = -np.log(b / I0)
        concentration = (A - intercept_B) / slope_B
    elif channels == "RGB":
        r = int(input(f"Please enter the R value of the sample {unknown_sample_names[i]} to be analyzed"))
        g = int(input(f"Please enter the G value of the sample {unknown_sample_names[i]} to be analyzed"))
        b = int(input(f"Please enter the B value of the sample {unknown_sample_names[i]} to be analyzed "))
        A = -np.log(np.mean([r, g, b]) / I0)
        concentration = (A - intercept_RGB) / slope_RGB
    elif channels == "RG":
        r = int(input(f"Please enter the R value of the sample {unknown_sample_names[i]} to be analyzed "))
        g = int(input(f"Please enter the G value of the sample {unknown_sample_names[i]} to be analyzed"))
        A = -np.log(np.mean([r, g]) / I0)
        concentration = (A - intercept_RG) / slope_RG
    elif channels == "RB":
        r = int(input(f"Please enter the R value of the sample {unknown_sample_names[i]} to be analyzed"))
        b = int(input(f"Please enter the B value of the sample {unknown_sample_names[i]} to be analyzed"))
        A = -np.log(np.mean([r, b]) / I0)
        concentration = (A - intercept_RB) / slope_RB
    elif channels == "GB":
        g = int(input(f"Please enter the G value of the sample {unknown_sample_names[i]} to be analyzed"))
        b = int(input(f"Please enter the B value of the sample {unknown_sample_names[i]} to be analyzed"))
        A = -np.log(np.mean([g, b]) / I0)
        concentration = (A - intercept_GB) / slope_GB
        
    unknown_concentrations.append(concentration)

# Create a table with the results using pandas
results_df = pd.DataFrame({"Sample": unknown_sample_names, f"Concentration ({unit})": unknown_concentrations})

# Set the index of the DataFrame to start at 1
results_df.index = results_df.index + 1

print(f"\nConcentrations of samples to be analyzed ({unit}):")
print(results_df)

# Prompt the user for a document name
excel_file = input("Please enter a document name to save:") + '.xlsx'

# Adjust the column name to add the unit of measure
results_df = results_df.rename(columns={"Concentration": f"Concentration ({unit})"})

# Save the obtained data in Microsoft Excel document format
with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
    results_df.to_excel(writer, sheet_name='Results', index_label='No.')

print(f"Results are saved in Microsoft Excel file '{excel_file}'.")




 
