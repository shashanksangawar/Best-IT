<?php
    include '../includes/template.html';
    if($_SERVER["REQUEST_METHOD"]=="POST")
    {
        $json_data = file_get_contents("php://input");
        $data = json_decode($json_data, true);
        echo "<h1>".$json_data."</h1>";
    }
?>

</main></div>
</body>
</html>