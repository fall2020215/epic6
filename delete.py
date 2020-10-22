import csv
def delete_application(name, title):
    
    st = []
    with open("data_app.csv","r") as file:
        reader_csv = csv.reader(file)
        for row in reader_csv:
            if row != [] and (row[0] != name or row[1] != title):
                st.append(tuple(row))

    with open("data_app.csv","w") as file:
        writer_csv = csv.writer(file)
        for element in st:
            writer_csv.writerow(element)

delete_application("quynh","math")
