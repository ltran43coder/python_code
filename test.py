import math
import pandas as pd
from pandas import DataFrame

input_table_1 = pd.read_excel('C:/LAM/PY_PROJ/excel/test2.xlsx')
# print(input_table_1)
# print(input_table_1['GAP'])
# print(input_table_1['Assign Qty'])

#if cot J GAP > 0, cot K Adjst Assignment lay ket qua cot H Assign Prio
for ind in input_table_1.index:
    if input_table_1["GAP"][ind] >= 0:
        input_table_1.loc[ind, "Adjst Assignment"] = input_table_1["Assign Prio"][ind]
        # input_table_1.iloc[ind, 10] = input_table_1["Assign Prio"][ind]
        print("if ", input_table_1["Adjst Assignment"][ind])
    else:
        #if cot J < 0, cot K lay ket qua cot I SOH gia tri truoc do
        input_table_1.loc[ind, "Adjst Assignment"] = input_table_1["SOH"][ind-1]
        print("else ", input_table_1["Adjst Assignment"][ind])

input_table_1.to_excel('C:/LAM/PY_PROJ/excel/test2_result.xlsx', index = False, header=True)

# if input_table_1["Gap"] !> 0:
#     Adjst Assignment.append(input_table_1["Assign Qty"][each])
# else:
#     Adjst Assignment.append(input_table_1["Gap"][each - 1])[each])

