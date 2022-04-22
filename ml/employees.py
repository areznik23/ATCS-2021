import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('data5/employees.csv')
data['Gender'].replace(['Male', 'Female'], [0, 1], inplace=True)
data['OverTime'].replace(['No', 'Yes'], [0, 1], inplace=True)
# Age,Attrition,DailyRate,DistanceFromHome,Education,EnvironmentSatisfaction,Gender,HourlyRate,JobInvolvement,JobLevel,JobSatisfaction,MaritalStatus,MonthlyIncome,MonthlyRate,NumCompaniesWorked,Over18,OverTime,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,StandardHours,StockOptionLevel,TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager

# Age, DistanceFromHome, Gender, JobInvolvement, MaritalStatus, MonthlyIncome, Overtime, YearsAtCompany
# WorkLifeBalance

x = data[['Age', 'DistanceFromHome', 'Gender', 'JobInvolvement', 'MonthlyIncome', 'OverTime', 'YearsAtCompany']].values
y = data['WorkLifeBalance'].values

scaler = StandardScaler().fit(x)
x = scaler.transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = LinearRegression().fit(x_train, y_train)

predict = model.predict(x_test)

print("R Squared Value: ", round(model.score(x_train, y_train), 2), '\n')

# Age, DistanceFromHome, Gender, JobInvolvement, MaritalStatus, MonthlyIncome, Overtime, YearsAtCompany
print('Testing linear model with test data')
for i in range(len(x_test)):
    actual = y_test[i]
    y_pred = round(predict[i], 2)
    x_age = x_test[i][0]
    x_distance_from_home = x_test[i][1]
    x_gender = x_test[i][2]
    x_job_involvement = x_test[i][3]
    x_monthly_income = x_test[i][4]
    x_overtime = x_test[i][5]
    x_years_at_company = x_test[i][6]
    print(
        "Age:", float(x_age),
        "Distance from home: ", float(x_distance_from_home),
        "Gender:", float(x_gender),
        "Job Involvement: ", float(x_job_involvement),
        "Monthly Income: ", float(x_monthly_income),
        "Overtime: ", float(x_overtime),
        'Years at Company: ', float(x_years_at_company),
        "predict y val: ", y_pred,
        "actual y val:", actual
    )

print('New Predictions \n')
new_test = [[40, 50, 0, 5, 20000, 0, 10]]
pred = model.predict(new_test)
for i in range(len(new_test)):
    actual = y_test[i]
    y_pred = round(float(pred), 2)
    x_age = new_test[i][0]
    x_distance_from_home = new_test[i][1]
    x_gender = new_test[i][2]
    x_job_involvement = new_test[i][3]
    x_monthly_income = new_test[i][4]
    x_overtime = new_test[i][5]
    x_years_at_company = new_test[i][6]
    print(
        "Age:", float(x_age),
        "Distance from home: ", float(x_distance_from_home),
        "Gender:", float(x_gender),
        "Job Involvement: ", float(x_job_involvement),
        "Monthly Income: ", float(x_monthly_income),
        "Overtime: ", float(x_overtime),
        'Years at Company: ', float(x_years_at_company),
        "predict y val: ", y_pred
    )
