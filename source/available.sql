CREATE TABLE product_details (
    SerialNo VARCHAR(100) PRIMARY KEY,
    PurchaseDate DATETIME, 
    CompanyName VARCHAR(50), 
    ModelName VARCHAR(50), 
    Processor VARCHAR(50),
    SSD VARCHAR(10), 
    HDD VARCHAR(10), 
    RAM VARCHAR(10), 
    Supplier VARCHAR(100),
    AvailableAt VARCHAR(70)
);

CREATE TABLE product_issues (
    SerialNum VARCHAR(100),
    Issue VARCHAR(255),
    FOREIGN KEY (SerialNum) REFERENCES product_details(SerialNo)
);

