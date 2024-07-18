student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# lopping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key, value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# loo though a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# for (index, row) in student_data_frame.iterrows():
#     print(index, row)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(type(row.score), row.score)