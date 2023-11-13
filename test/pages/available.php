<?php
include '../includes/template.html';
?>

<?php

// SQL Connector
$db_host = "127.0.0.1"; 
$db_user = "root";
$db_password = "admin";
$db_name = "STOCK_AVAILABLE";

$db = new mysqli($db_host, $db_user, $db_password, $db_name);
if($db->connect_error)
{
    die("Database Connection failed: " . $db->connect_error);
}

// Insert Queries
$query1 = "SELECT * FROM product_details u, product_images a WHERE a.SerialNum=u.SerialNo";
$result = $db->query($query1);

if ($result) 
{
    while ($row = $result->fetch_assoc()) {
        echo '<div class="card">';
        foreach ($row as $columnName => $columnValue) {
            if ($columnName == "Device" || $columnName == "ImageProof") {
                // If it's one of the image columns, display the image
                echo '<img src="data:image/jpeg;base64,' . base64_encode($columnValue) . '">';
            }
            else {
                // Display other non-image data
                echo '<p>' . $columnName . ': ' . $columnValue . '</p>';
            }
        }
        echo '<div class="container-buttons">';
        echo '<button class="issue" onclick="redirectToIssuePage(' . json_encode($row) . '){window.location.href = "/issue.php?product=" + product_issue;}">Issue</button>';
        echo '<button class="sell" onclick="redirectToSellPage(' .  json_encode($row)  . ')">Sell</button>';
        echo '</div>';
        echo '</div>';
    }
    $result->close();
} 
else 
{
    echo "Error: " . $db->error;
}

$db->close();
?>


</main></div>   

<!-- Modal for Issue -->
<div class="modal fade" id="issueModal" tabindex="-1" role="dialog" aria-labelledby="issueModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="issueModalLabel">Enter Issue Details</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <textarea id="issueDetails" class="form-control" rows="4" placeholder="Enter issue details"></textarea>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" onclick="submitIssue()">Submit</button>
            </div>
        </div>
    </div>
</div>

<!-- Modal for Sell -->
<div class="modal fade" id="sellModal" tabindex="-1" role="dialog" aria-labelledby="sellModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="sellModalLabel">Enter Customer Details</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <input type="text" id="sellDate" class="form-control" placeholder="Enter Selling Date (YYYY-MM-DD)">
                <input type="text" id="customerName" class="form-control" placeholder="Enter customer name">
                <input type="text" id="customerContact" class="form-control" placeholder="Enter customer contact">
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" onclick="submitSell()">Submit</button>
            </div>
        </div>
    </div>
</div>

<script>
    $(document).ready(function() {
        // Function to open the Issue modal
        function redirectToIssuePage(product_issue) {
            // Assuming you want to redirect to issue.php, change the URL accordingly
            window.location.href = '/issue.php?product=' + product_issue;
        }

        // Function to open the Sell modal
        function redirectToSellPage(product_sell) {
            // Assuming you want to redirect to sell.php, change the URL accordingly
            window.location.href = '/sell.php?product=' + product_sell;
        }

        // Rest of your code for modal dialogs and AJAX requests
    });


    // Function to open the Issue modal
    // function redirectToIssuePage(product_issue) {
    //     console.log('Product Data:', product_issue);
    //     var currentProduct_issue = product_issue;
    //     $('#issueModal').modal('show');
    // }

    // // Function to submit the issue form
    // function submitIssue() {
    //     var issueDetails = document.getElementById('issueDetails').value;
    //     var product_details_issue = currentProduct_issue;
    //     // Send the customer name to the /sell route
    //     // Create a JavaScript object with data
    //     var dataToSend = {
    //         "issues": issueDetails,
    //         "type": "Available",
    //         "product": product_details_issue
    //         // Add any other data you want to send
    //     };

    //     // Make a POST request with JSON data
    //     $.ajax({
    //         url: '/issue.php',
    //         type: 'POST',
    //         contentType: 'application/json',
    //         data: JSON.stringify(dataToSend),
    //         success: function (response) {
    //             // Handle the response from the server
    //             console.log(response);
    //         }
    //     });
    //     // Close the modal
    //     $('#issueModal').modal('hide');
    // }

    // // Function to open the Sell modal
    // function redirectToSellPage(product_sell) {
    //     var currentProduct_sell = product_sell;
    //     $('#sellModal').modal('show');
    // }

    // // Function to submit the sell form
    // function submitSell() {
    //     var customerName = document.getElementById('customerName').value;
    //     var customerContact = document.getElementById('customerContact').value;
    //     var sellDate = document.getElementById('sellDate').value;
    //     var product = currentProduct_sell;
    //     // Send the customer name to the /sell route
    //     // Create a JavaScript object with data
    //     var dataToSend = {
    //         "selling_date": sellDate,
    //         "customer_name": customerName,
    //         "customer_contact": customerContact,
    //         "product": product
    //         // Add any other data you want to send
    //     };

    //     // Make a POST request with JSON data
    //     $.ajax({
    //         url: '/sell.php',
    //         type: 'POST',
    //         contentType: 'application/json',
    //         data: JSON.stringify(dataToSend),
    //         success: function (response) {
    //             // Handle the response from the server
    //             console.log(response);
    //         }
    //     });
    //     // Close the modal
    //     $('#sellModal').modal('hide');
    // }

 
</script>
</body>
</html>