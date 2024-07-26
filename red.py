import streamlit as st
import pandas as pd
import pymysql

# Function to connect to MySQL and execute a query
def execute_query(query, params=None):
    myconnection = pymysql.connect(host='127.0.0.1', user='root', passwd='Admin@Yunus111', database='project_1')
    try:
        df = pd.read_sql(query, myconnection, params=params)
        return df
    except Exception as e: #block used for handling exceptions
        st.error(f"Error: {e}") # to display an error message
        return pd.DataFrame() #returns an empty DataFrame
    finally:
        myconnection.close()

# Function to generate SQL query based on filters
def generate_query(bustype, route, price_min, price_max, rating_min, rating_max, availability):
    query = "SELECT * FROM redbus WHERE 1=1"
    
    if bustype:
        bustype_str = ",".join(["%s"] * len(bustype))
        query += f" AND Bus_Type IN ({bustype_str})"
    if route:
        route_str = ",".join(["%s"] * len(route))
        query += f" AND Bus_Route IN ({route_str})"
    if price_min is not None:
        query += f" AND Fare >= {price_min}"
    if price_max is not None:
        query += f" AND Fare <= {price_max}"
    if rating_min is not None:
        query += f" AND Rating >= {rating_min}"
    if rating_max is not None:
        query += f" AND Rating <= {rating_max}"
    if availability is not None:
        query += f" AND Seat_Availability >= {availability}"
    
    return query

# Streamlit application
def main():
    st.title('RedBus Data Filter')
    st.sidebar.header('Filter Options')

    # Fetch unique values for filters
    bustypes_df = execute_query("SELECT DISTINCT Bus_Type FROM redbus")
    routes_df = execute_query("SELECT DISTINCT Bus_Route FROM redbus")

    # Ensure the columns exist
    if 'Bus_Type' in bustypes_df.columns and 'Bus_Route' in routes_df.columns:
        bustypes = bustypes_df['Bus_Type'].tolist()
        routes = routes_df['Bus_Route'].tolist()
    else:
        st.error("The necessary columns were not found in the database.")
        return

    # Sidebar filters
    selected_bustypes = st.sidebar.multiselect("Bus Type", bustypes)
    selected_routes = st.sidebar.multiselect("Bus Route", routes)
    price_range = st.sidebar.slider("Price Range", 0, 5000, (0, 5000))
    rating_range = st.sidebar.slider("Star Rating", 0.0, 5.0, (0.0, 5.0))
    availability = st.sidebar.number_input("Minimum Availability", min_value=0, value=0, step=1)

    # Generate and execute query
    query = generate_query(
        selected_bustypes,
        selected_routes,
        price_range[0],
        price_range[1],
        rating_range[0],
        rating_range[1],
        availability
    )
    
    params = selected_bustypes + selected_routes
    filtered_df = execute_query(query, params)
    
    # Display the filtered data
    st.subheader('Filtered Data')
    st.write(filtered_df)

if __name__ == '__main__':
    main()