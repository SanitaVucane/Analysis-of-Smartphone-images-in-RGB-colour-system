#### Project name: Analysis of smartphone images for the determination of total phenols in Vegetable oils

### Analysis of Smartphone Images for the Determination of Total Phenols in Vegetable Oils

This project provides a Python-based tool for analyzing the total phenol content in vegetable oils using RGB values from smartphone images. The RGB color system is utilized to calculate absorption values, which are then correlated with phenol concentrations through a series of calibration curves.

## Features

- **RGB Absorption Calculation**: Automatically calculates the absorption values for R, G, and B channels using intensity data.
- **Calibration Curves**: Generates calibration curves for different combinations of RGB channels (R, G, B, RGB, RG, RB, GB) using linear regression.
- **Concentration Calculation**: Estimates phenol concentration in unknown samples based on the RGB values and the generated calibration curves.
- **User-Interactive Input**: The program prompts users to input concentration units, calibration data, and unknown sample details.
- **Visualization**: Graphical calibration curves are created for easy visualization of the relationship between absorption and concentration.
- **Data Export**: Results are saved in an Excel file, allowing users to easily store and share the analyzed data.

## Workflow

1. **Input**: Users enter the RGB values for a set of known calibration solutions.
2. **Absorption Calculation**: Absorption is computed for each RGB channel.
3. **Calibration**: Linear regression is applied to generate calibration equations, with R² values for each color channel.
4. **Analysis of Unknown Samples**: Users input the RGB values for unknown samples, and the tool calculates the phenol concentration based on the selected color channel(s).
5. **Output**: Results are saved in an Excel file.

## Example Usage

1. Input the concentration unit and RGB values for calibration solutions.
2. Select a color channel (R, G, B, or combinations) for the calibration and analysis of unknown samples.
3. Input the RGB values of unknown samples to get the estimated concentrations.
4. Save the results in an Excel file.

## Dependencies

- Python 3.x
- NumPy
- Pandas
- Matplotlib
- SciPy
- Openpyxl

```bash
pip install numpy pandas matplotlib scipy openpyxl
```
## License

This project is licensed under the **GNU General Public License v3.0**. You are free to use, modify, and distribute the code for academic and non-commercial purposes. However, any commercial usage may require a separate license.

## Limitations

- The accuracy of the analysis depends on the quality of smartphone images and the consistency of lighting conditions during image capture.
- The algorithm is designed for research purposes and may not be suitable for commercial use without further validation.
- Different smartphones may yield slightly different results due to variations in camera quality and RGB sensor calibration.

## Contributions

Contributions, bug reports, and improvements are welcome! If you'd like to contribute, please fork the repository, create a new branch, and submit a pull request with your proposed changes.


