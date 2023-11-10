<?php
include '../includes/template.html';
?>

<form method="post" enctype="multipart/form-data" class="form">
       <div class="container">
        Serial Number: <input type="text" name="serial_no" placeholder="Serial Number" required class="inputs"><br><br>
        Purchase Date: <input type="text" name="date" placeholder="Purchase Date" required class="inputs"><br><br>
        Company Name: <input type="text" name="company_name" placeholder="Company Name" required class="inputs"><br><br>
        Model Name: <input type="text" name="model_name" placeholder="Model Name" required class="inputs"><br><br>
        Processor: <input type="text" name="processor" placeholder="Processor" required class="inputs"><br><br>
        <div class="inside-container">
            SSD: <input type="text" name="ssd" placeholder="SSD" class="inputs"><br><br>
            HDD: <input type="text" name="hdd" placeholder="HDD" class="inputs-2"><br><br>
            RAM: <input type="text" name="ram" placeholder="RAM" required class="inputs-2"><br><br>
            Supplier Name: <input type="text" name="supplier" placeholder="Supplier Name" required class="inputs-2"><br><br>
            Device Available at: <input type="text" name="available_at" placeholder="Device Available at" required class="inputs-2"><br><br>
        </div>
         Device Proof: <input type="file" name="device" accept="image/*" required><br><br>
        Image Proof: <input type="file" name="image_proof" accept="image/*" required><br><br>
        
        <br><br>

       </div>
       <div class="container-2">
        <input type="submit" value="Submit Item" class="inputs-button">

       </div>
    </form>
</main></div>

<?php

if($_SERVER["REQUEST_METHOD"]=="POST")
{
    // Retrive Form data
    $serial_no = $_POST["serial_no"];
    $date = $_POST["date"];
    $company_name = $_POST["company_name"];
    $model_name = $_POST["model_name"];
    $processor = $_POST["processor"];
    $ssd = $_POST["ssd"];
    $hdd = $_POST["hdd"];
    $ram = $_POST["ram"];
    $supplier = $_POST["supplier"];
    $available_at = $_POST["available_at"];

    $device = file_get_contents($_FILES["device"]["tmp_name"]);
    $image_proof = file_get_contents($_FILES["image_proof"]["tmp_name"]);
    
    
    // SQL Connector
    $db_host = "127.0.0.1"; 
    $db_user = "eminence";
    $db_password = "shadosama";
    $db_name = "STOCK_AVAILABLE";

    $db = new mysqli($db_host, $db_user, $db_password, $db_name);
    if($db->connect_error)
    {
        die("Database Connection failed: " . $db->connect_error);
    }

    // Insert Queries
    $query1 = "INSERT INTO product_details(SerialNo, PurchaseDate, CompanyName, ModelName, Processor, SSD, HDD, RAM, Supplier, AvailableAt) VALUES (?, ?, ?, ?, ? ,?, ?, ?, ?, ?)";
    $stmt1 = $db->prepare($query1);
    $stmt1->bind_param("ssssssssss", $serial_no, $date, $company_name, $model_name, $processor, $ssd, $hdd, $ram, $supplier, $available_at);

    if ($stmt1->execute()) 
    {
        $stmt1->close();
        $query2 = "INSERT INTO product_images(SerialNum, Device, ImageProof) VALUES (?, ?, ?)";
        $stmt2 = $db->prepare($query2);
        $stmt2->bind_param("sss", $serial_no, $device, $image_proof);

        if ($stmt2->execute()) 
        {
            echo "Data Inserted Successfully";
        } 
        else 
        {
            echo "Error: " . $stmt->error;
        }

        $stmt2->close();
    } 
    else 
    {
        echo "Error: " . $stmt->error;
    }

    

    $db->close();
}

?>
