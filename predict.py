import seaborn as sns
from sklearn.linear_model import LinearRegression
import pandas as pd
iris_data=sns.load_dataset("iris")
x=iris_data.petal_width.as_matrix(columns=None)
x=x.reshape(-1,1)
lm=LinearRegression()
model=lm.fit(x,iris_data.petal_length)
def function_predict(petal_width):
	petal_width=int(petal_width)
	prediction_data=pd.DataFrame({"petal_width":[petal_width]})
	return(lm.predict(prediction_data))