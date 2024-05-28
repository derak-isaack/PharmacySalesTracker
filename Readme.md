## <div style="padding: 35px;color:white;margin:10;font-size:200%;text-align:center;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://images.pexels.com/photos/7078619/pexels-photo-7078619.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)"><b><span style='color:black'><strong> ETL Pipeline Pharmacy sales Tracker</strong></span></b> </div> 

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)
![streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=fff&style=for-the-badge)
![GoogleSheets](https://img.shields.io/badge/Google%20Sheets-34A853?logo=googlesheets&logoColor=fff&style=for-the-badge)
![Duckdb](https://img.shields.io/badge/DuckDB-FFF000?logo=duckdb&logoColor=000&style=for-the-badge)
![DBT](https://img.shields.io/badge/dbt-FF694B?logo=dbt&logoColor=fff&style=for-the-badge)
![Jinja](https://img.shields.io/badge/Jinja-B41717?logo=jinja&logoColor=fff&style=for-the-badge)

### <div style="padding: 20px;color:white;margin:10;font-size:90%;text-align:left;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://w0.peakpx.com/wallpaper/957/661/HD-wallpaper-white-marble-white-stone-texture-marble-stone-background-white-stone.jpg)"><b><span style='color:black'> Overview</span></b> </div>

This is a `Pharmacy Sales tracker` which connects `Streamlit` and `Google Sheets`. The `Streamlit` application provides a user interphace for the employees to input the product quantity sales of a pharmaceutical company across several distributed towns. 

The `User Interface` looks like:
![Demo](<Screenshot (964).png>)

After employee input about sales, the same sheet is extracted and loaded into an `OLAP` database precisely `DuckDB` where `DBT` is used to perform transformation of the sales data which can be found [here](models). 

`DUCKDB` is efficient for handling large volumes of data and scales well with any type of data. 

With sufficient data, an `increemental model` using `DNT` will be implemented to only ensure new incoming data is transformed so as not to slow the database operations. 

`DBT` is a good tool for transformartion as it allows building efficient scalable `ETL` data pipelines. With DBT, different transformation `SQL` models can be chained together through model referencing. 


### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
