import numpy as np
import matplotlib.pyplot as plt
import csv
from sklearn.svm import SVR

dates = []
prices = []

def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[1]))
    return

def predict_prices(dates, prices, x):
    dates = np.reshape(dates,(len(dates), 1))

    svr_lin = SVR(kernel= 'linear', C=1e3)
    svr_poly = SVR(kernel = 'poly', C=1e3, degree=2)
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    svr_lin.fit(dates, prices)
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)

    plt.scatter(dates, prices, color='black', label='Data')
    plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
    plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear Model')
    plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial Model')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()

    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

get_data('TSLA.csv')

predicted_price = predict_prices(dates, prices, 29)

print(predicted_price)


# OLD CODE
# # load data
# company = 'FB'

# start = dt.datetime(2012, 1, 1)
# end = dt.datetime(2022, 1, 1)

# data = web.DataReader(company, 'yahoo', start, end)

# # Prepare Data
# scaler = MinMaxScaler(feature_range=(0,1))
# scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1,1))

# prediction_days = 60

# x_train = []
# y_train = []

# for x in range(prediction_days, len(scaled_data)):
#     x_train.append(scaled_data[x-prediction_days: x, 0])
#     y_train.append(scaled_data[x, 0])

# x_train, y_train = np.array(x_train), np.array(y_train)
# x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# # Build the Models
# model = Sequential()

# model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1,)))
# model.add(Dropout(0,2))
# model.add(LSTM(units=50, return_sequences=True))
# model.add(Dropout(0,2))
# model.add(LSTM(units=50))
# model.add(Dropout(0,2))
# model.add(Dense(units=1)) # Prediction of the next closing value

# model.compile(optimizer='adam', loss='mean_squared_error')
# model.fit(x_train, y_train, epochs=6, batch_size=32)

# ''' TEST THE MODEL ACCURACY ON EXISTING DATA '''

# # Load Test Data
# test_start = dt.datetime(2022, 1, 1)
# test_end = dt.datetime.now()

# test_data = web.DataReader(company, 'yahoo', test_start, test_end)

# actual_prices = test_data['Close'].values

# total_dataset = pd.concat((data['Close'], test_data['Close']), axis=0)

# model_inputs = total_dataset[len(total_dataset) - len(test_data) - prediction_days:].values
# model_inputs = model_inputs.reshape(-1, 1)
# model_inputs = scaler.transform(model_inputs)

# # Make Predictions

# x_test = []

# for x in range(prediction_days, len(model_inputs)):
#     x_test.append(model_inputs[x-prediction_days:x, 0])

# x_test = np.array(x_test)
# x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# predicted_prices = model.predict(x_test)
# predicted_prices = scaler.inverse_transform(predicted_prices)

# # Plot The Test Predictions
# plt.plot(actual_prices, color="black", label=f"Actual {company} Price")
# plt.plot(predicted_prices, color="green", label=f"Predicted {company} Price")
# plt.title(f"{company} Share Price")
# plt.xLabel('Time')
# plt.yLabel(f"{company} Share Price")
# plt.legend()
# plt.show()
