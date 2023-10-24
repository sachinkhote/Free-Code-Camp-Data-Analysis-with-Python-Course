import numpy as np


def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  ls = np.array(list)
  mean_rows = [
      ls[[0, 1, 2]].mean(axis=0), ls[[3, 4, 5]].mean(axis=0),
      ls[[6, 7, 8]].mean(axis=0)
  ]
  mean_columns = [
      ls[[0, 3, 6]].mean(axis=0), ls[[1, 4, 7]].mean(axis=0),
      ls[[2, 5, 8]].mean(axis=0)
  ]
  var_rows = [
      ls[[0, 1, 2]].var(axis=0), ls[[3, 4, 5]].var(axis=0), ls[[6, 7,
                                                                8]].var(axis=0)
  ]
  var_columns = [
      ls[[0, 3, 6]].var(axis=0), ls[[1, 4, 7]].var(axis=0), ls[[2, 5,
                                                                8]].var(axis=0)
  ]
  std_rows = [
      ls[[0, 1, 2]].std(axis=0), ls[[3, 4, 5]].std(axis=0), ls[[6, 7,
                                                                8]].std(axis=0)
  ]
  std_columns = [
      ls[[0, 3, 6]].std(axis=0), ls[[1, 4, 7]].std(axis=0), ls[[2, 5,
                                                                8]].std(axis=0)
  ]
  max_rows = [
      ls[[0, 1, 2]].max(axis=0), ls[[3, 4, 5]].max(axis=0), ls[[6, 7,
                                                                8]].max(axis=0)
  ]
  max_columns = [
      ls[[0, 3, 6]].max(axis=0), ls[[1, 4, 7]].max(axis=0), ls[[2, 5,
                                                                8]].max(axis=0)
  ]
  min_rows = [
      ls[[0, 1, 2]].min(axis=0), ls[[3, 4, 5]].min(axis=0), ls[[6, 7,
                                                                8]].min(axis=0)
  ]
  min_columns = [
      ls[[0, 3, 6]].min(axis=0), ls[[1, 4, 7]].min(axis=0), ls[[2, 5,
                                                                8]].min(axis=0)
  ]
  sum_rows = [
      ls[[0, 1, 2]].sum(axis=0), ls[[3, 4, 5]].sum(axis=0), ls[[6, 7,
                                                                8]].sum(axis=0)
  ]
  sum_columns = [
      ls[[0, 3, 6]].sum(axis=0), ls[[1, 4, 7]].sum(axis=0), ls[[2, 5,
                                                                8]].sum(axis=0)
  ]

  return {
      'mean': [mean_columns, mean_rows, ls.mean()],
      'variance': [var_columns, var_rows, ls.var()],
      'standard deviation': [std_columns, std_rows,
                             ls.std()],
      'max': [max_columns, max_rows, ls.max()],
      'min': [min_columns, min_rows, ls.min()],
      'sum': [sum_columns, sum_rows, ls.sum()]
  }
