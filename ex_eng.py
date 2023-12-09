# import pandas as pd
# import re

# # Sample DataFrame
# def extract_english_text(input_text):
#     # Use regex to extract English text
#     english_text = re.sub(r'[^a-zA-Z\s]', '', input_text)
    
#     return english_text

# # Example text

# # Extract English text using regex

# # Print the result

# df = pd.read_csv('yellodata.csv')

# # Function to extract English text using regex
# z=0
# for i in range(len(df['Google Adress'])):
#     try:
#         df['Google Adress'][i] = extract_english_text(df['Google Adress'][i])
#     except:continue
#     z+=1
#     print(f"Saving-----  {z}")
# # Apply the function to the 'text_column' of the DataFrame
# df.to_csv('yellodata_finaleng.csv', index=False)
import pandas as pd





# Load the first CSV file
file1 = 'amazon_400k_asin_py_vs.csv'
df1 = pd.read_csv(file1)

# Load the second CSV file
file2 = 'amazon_200k_asin_a_vscode.csv'
df2 = pd.read_csv(file2)

# Concatenate the two DataFrames vertically
result_df = pd.concat([df1, df2], ignore_index=True)

# Save the result to a new CSV file
result_df.to_csv('amazon_400k_asins_final.csv', index=False)

# # Print a message indicating success
# print("Files successfully merged and saved to 'merged_files.csv'")