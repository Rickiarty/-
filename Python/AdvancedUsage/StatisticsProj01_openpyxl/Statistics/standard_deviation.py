from Statistics.variance import variance

def standard_deviation_from_known_variance(variance) -> float:
    return variance ** 0.5

def standard_deviation(worksheet, aver_cell, range_cells) -> float:
    var = variance(worksheet, aver_cell, range_cells)
    return var ** 0.5
