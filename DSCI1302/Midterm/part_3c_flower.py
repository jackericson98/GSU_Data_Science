import pandas as pd

iris = pd.read_csv("part_3_data/iris.csv")

setosa = iris[iris["Flower_class"] == "Iris-setosa"]
versicolor = iris[iris["Flower_class"] == "Iris-versicolor"]
virginica = iris[iris["Flower_class"] == "Iris-virginica"]

# What is the median petal length and width for each flower type?

setosa_med_petal_len = setosa["Sepal_length"].median()
setosa_med_petal_wid = setosa["Sepal_width"].median()
versicolor_med_petal_len = versicolor["Sepal_length"].median()
versicolor_med_petal_wid = versicolor["Sepal_width"].median()
virginica_med_petal_len = virginica["Sepal_length"].median()
virginica_med_petal_wid = virginica["Sepal_width"].median()

# Lazy Print help
data = [[setosa_med_petal_len, setosa_med_petal_wid], [versicolor_med_petal_len, versicolor_med_petal_wid],
        [virginica_med_petal_len, virginica_med_petal_wid]]
for i in range(3):
    if i == 0:
        flower = "Setosa"
    elif i == 1:
        flower = "Versicolor"
    else:
        flower = "Virginica"
    print("\n{}'s' median petal length is: {}.\n{} median petal width is: {}"
          .format(flower, data[i][0], flower, data[i][1]))


# What is the correlation for each flower type?

print("\n\nSetosa attribute correlations:\n {}\n\nVersicolor attribute correlations:\n {}\n\nVirginica attribute "
      "correlations:\n {}".format(setosa.corr(), versicolor.corr(), virginica.corr()))
