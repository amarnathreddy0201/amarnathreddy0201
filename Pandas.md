# 📊 Pandas Functions Cheat Sheet

A quick reference guide for commonly used **Pandas functions**, organized by category.  

---

## 🔹 1. Import & Basics
| Function | Description |
|----------|-------------|
| `import pandas as pd` | Import pandas library |
| `pd.Series(data)` | Create 1D labeled array |
| `pd.DataFrame(data)` | Create 2D labeled table |

---

## 🔹 2. Data I/O (Input / Output)
| Function | Description |
|----------|-------------|
| `pd.read_csv("file.csv")` | Read CSV file |
| `df.to_csv("file.csv")` | Save to CSV |
| `pd.read_excel("file.xlsx")` | Read Excel file |
| `df.to_excel("file.xlsx")` | Save to Excel |
| `pd.read_json("file.json")` | Read JSON file |
| `df.to_json("file.json")` | Save to JSON |
| `pd.read_sql(query, conn)` | Read from SQL database |

---

## 🔹 3. Data Inspection
| Function | Description |
|----------|-------------|
| `df.head(n)` | Show first n rows |
| `df.tail(n)` | Show last n rows |
| `df.info()` | Summary of dataframe |
| `df.shape` | Number of rows & columns |
| `df.columns` | List column names |
| `df.dtypes` | Show data types |
| `df.describe()` | Summary statistics |

---

## 🔹 4. Selection & Indexing
| Function | Description |
|----------|-------------|
| `df['col']` | Select single column |
| `df[['col1','col2']]` | Select multiple columns |
| `df.loc[row, col]` | Select by labels |
| `df.iloc[row, col]` | Select by index |
| `df.at[row, col]` | Fast access by label |
| `df.iat[row, col]` | Fast access by index |

---

## 🔹 5. Filtering & Boolean Indexing
| Function | Description |
|----------|-------------|
| `df[df['col'] > 5]` | Filter rows |
| `df[(df['col1'] > 5) & (df['col2'] < 10)]` | Multiple conditions |
| `df.query("col1 > 5 and col2 < 10")` | Query expression |

---

## 🔹 6. Data Cleaning
| Function | Description |
|----------|-------------|
| `df.isnull()` | Check missing values |
| `df.dropna()` | Drop missing values |
| `df.fillna(value)` | Fill missing values |
| `df.duplicated()` | Find duplicates |
| `df.drop_duplicates()` | Remove duplicates |
| `df.replace(old, new)` | Replace values |

---

## 🔹 7. Column & Row Operations
| Function | Description |
|----------|-------------|
| `df['new'] = df['col1'] + df['col2']` | Create new column |
| `df.rename(columns={'old':'new'})` | Rename columns |
| `df.drop('col', axis=1)` | Drop column |
| `df.drop(index=5)` | Drop row |
| `df.sort_values('col')` | Sort by column |
| `df.sort_index()` | Sort by index |

---

## 🔹 8. Grouping & Aggregation
| Function | Description |
|----------|-------------|
| `df.groupby('col').mean()` | Group by column and average |
| `df.groupby('col').agg({'col1':'sum','col2':'max'})` | Multiple aggregations |
| `df['col'].value_counts()` | Count unique values |
| `df.pivot_table(values='val', index='row', columns='col', aggfunc='mean')` | Pivot table |

---

## 🔹 9. Merging & Joining
| Function | Description |
|----------|-------------|
| `pd.concat([df1, df2])` | Concatenate dataframes |
| `pd.merge(df1, df2, on='key')` | Merge on column key |
| `df1.join(df2, on='key')` | Join on index or key |

---

## 🔹 10. Time Series
| Function | Description |
|----------|-------------|
| `pd.to_datetime(df['date'])` | Convert to datetime |
| `df['date'].dt.year` | Extract year |
| `df['date'].dt.month` | Extract month |
| `df.resample('M').mean()` | Resample monthly |

---

## 🔹 11. Statistics
| Function | Description |
|----------|-------------|
| `df.mean()` | Mean |
| `df.median()` | Median |
| `df.std()` | Standard deviation |
| `df.min() / df.max()` | Minimum / Maximum |
| `df.corr()` | Correlation matrix |
| `df.cov()` | Covariance matrix |

---

## 🔹 12. Visualization (with Matplotlib)
| Function | Description |
|----------|-------------|
| `df['col'].plot()` | Line plot |
| `df['col'].hist()` | Histogram |
| `df.plot.scatter(x='col1', y='col2')` | Scatter plot |

---


## 🔹13. What is series in pandas

A Series in pandas is a one-dimensional labeled array that holds data along with an index. It is similar to a single column in a table.”

Example:

import pandas as pd

marks = pd.Series([85, 90, 78], index=['Alice', 'Bob', 'Charlie'])
print(marks)
