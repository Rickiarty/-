from openpyxl import load_workbook

def single_variance_unit(xi, average) -> float:
    return (xi - average) ** 2

def variance(worksheet, aver_cell, range_cells) -> float:
    var = 0

    aver = float(worksheet[aver_cell].value)
    for coord in range_cells:
        if worksheet[coord].value != None and worksheet[coord].value != "":
            xi = float(worksheet[coord].value)
            var += single_variance_unit(xi, average=aver)
    divisor = len(range_cells) - 1 
    if divisor > 0:
        var /= divisor
    
    return var
