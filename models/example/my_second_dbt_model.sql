
-- Use the `ref` function to select from other models

select  
    product,
    quantity_sold,
    price,
    Date,
    Name,
    Area,
    stock_remaining,
    quantity_sold * price as sales 
from {{ ref('my_first_dbt_model') }}

