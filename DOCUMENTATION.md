# day1
## UNDERSTAND & EXPLORE THE DATA
after exploring the data i found that the columns are
    `['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode',
       'Customer ID', 'Customer Name', 'Segment', 'Country', 'City', 'State',
       'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category',
       'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit']`

there types are : 
    ```Row ID             int64
    Order ID             str
    Order Date           str
    Ship Date            str
    Ship Mode            str
    Customer ID          str
    Customer Name        str
    Segment              str
    Country              str
    City                 str
    State                str
    Postal Code          str
    Region               str
    Product ID           str
    Category             str
    Sub-Category         str
    Product Name         str
    Sales            float64
    Quantity         float64
    Discount         float64
    Profit           float64```

### suggested business rules
Customer Name → personal data

Discount > 100% → invalid  --not found

Quantity < 0 → invalid   --found

Ship Date < Order Date → invalid   --found

Missing values → must be analyzed and treated   --found

Duplicates → must be detected and treated  --found

Invalid date formats → must be detected  --found

Values outside logical ranges → must be detected  --found


