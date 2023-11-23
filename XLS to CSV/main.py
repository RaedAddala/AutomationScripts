import codecs

import pandas as pd


def capitalize_and_remove_redundant_spaces(text):
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)


def read_fields(input_file):
    fields = []
    try:
        with codecs.open("./" + input_file, "r", "UTF-8") as f:
            fields = f.read().splitlines()
    except FileNotFoundError as e:
        print(f"File Not found Error: {e}")
    return fields


def convert_excel_to_csv(excel_file, csv_file, input_fields, output_fieldname):
    try:
        df = pd.read_excel(excel_file)
        selected_input_df = df[input_fields]
        selected_output_df = pd.DataFrame(columns=[output_fieldname])
        for index, row in selected_input_df.iterrows():
            if index == 0:
                continue
            msg = ""
            for i in input_fields:
                msg += row[i] + " "
            selected_output_df.loc[
                len(selected_output_df.index)
            ] = capitalize_and_remove_redundant_spaces(msg)
        selected_output_df.to_csv(csv_file, index=False)
    except Exception as e:
        print(f"Error converting Excel file to CSV: {e}")


def main():
    excel_file = ""
    try:
        with codecs.open("./inputname.txt", "r", "UTF-8") as f:
            excel_file = f.readline().strip()
    except FileNotFoundError as e:
        print(f"File Not found Error: {e}")
    inputfields_file = "inputfields.txt"
    outputfields_file = "outputfieldName.txt"
    csv_file = "output.csv"

    input_fields = read_fields(inputfields_file)
    output_fields = read_fields(outputfields_file)[0]
    convert_excel_to_csv(excel_file, csv_file, input_fields, output_fields)


if __name__ == "__main__":
    main()
