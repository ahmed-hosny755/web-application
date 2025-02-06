file=open("model.pkl","rb")
model=pk.load(file)
import streamlit as st
import numpy as np

st.title('Diabetes Prediction Web Application')

# إنشاء واجهة تفاعلية
st.write("Enter values to predict the outcome:")
Pregnancies = st.number_input('Feature 1', min_value=float(data.min()[0]), max_value=float(data.max()[0]))
Glucose  = st.number_input('Feature 2', min_value=float(data.min()[1]), max_value=float(data.max()[1]))
BloodPressure = st.number_input('Feature 3', min_value=float(data.min()[2]), max_value=float(data.max()[2]))
SkinThickness = st.number_input('Feature 4', min_value=float(data.min()[3]), max_value=float(data.max()[3]))
Insulin = st.number_input('Feature 5', min_value=float(data.min()[4]), max_value=float(data.max()[4]))
BMI= st.number_input('Feature 5', min_value=float(data.min()[4]), max_value=float(data.max()[5]))
DiabetesPedigreeFunction= st.number_input('Feature 5', min_value=float(data.min()[4]), max_value=float(data.max()[5]))
Age= st.number_input('Feature 5', min_value=float(data.min()[4]), max_value=float(data.max()[5]))
Outcome= st.number_input('Feature 5', min_value=float(data.min()[4]), max_value=float(data.max()[5]))

# زر التنبؤ
if st.button('Predict'):
    input_data = np.array([[feature1, feature2, feature3, feature4, feature5]])
    prediction = model.predict(input_data)
    st.write(f"Prediction: {prediction[0]}")

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
st.write(f"Model Mean Squared Error: {mse}")

