import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Time Series Forecasting App",
        page_icon="📈"
        )

st.title("📈 Time Series Forecasting")

st.write("Forecast future airline passengers using ARIMA.")

model = joblib.load("forecast_model.pkl")

months = st.slider(
            "Select Number of Months to Forecast",
                min_value=1,
                    max_value=24,
                        value=12
                        )

if st.button("Generate Forecast"):
    forecast = model.forecast(steps=months)
    forecast_df = pd.DataFrame({"Forecasted Passengers": forecast
                                            })

st.subheader("Forecast Results")

                
st.dataframe(forecast_df)
st.subheader("Forecast Chart")

st.line_chart(forecast_df)