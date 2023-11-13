CREATE TABLE product_details (
    SerialNo VARCHAR(100) PRIMARY KEY,
    SellDate DATETIME, 
    CompanyName VARCHAR(50), 
    ModelName VARCHAR(50), 
    Processor VARCHAR(50),
    SSD VARCHAR(10), 
    HDD VARCHAR(10), 
    RAM VARCHAR(10), 
    CustomerName VARCHAR(100),
    CustomerContact VARCHAR(10)
);

CREATE TABLE product_issues (
    SerialNum VARCHAR(100),
    Issue VARCHAR(255),
    FOREIGN KEY (SerialNum) REFERENCES product_details(SerialNo)
);

CREATE TABLE product_images (
    SerialNum VARCHAR(100),
    Device LONGBLOB,
    ImageProof LONGBLOB,
    FOREIGN KEY (SerialNum) REFERENCES product_details(SerialNo)
);
