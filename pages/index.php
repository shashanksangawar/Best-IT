<!DOCTYPE html>
<html lang="en">

<head>
    <title>Best Computer</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="./css/main.css" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com?plugins=forms,typography,aspect-ratio"></script>
</head>

<body>
    <!-- Defining Macro for other html file -->
    <!-- Hero section -->
    <div class="hero w-full h-screen">

        <!-- Navbar -->
        <nav class="w-[300px] h-full bg-blue-300 fixed lg:flex flex-col justify-between items-center py-[2rem] hidden"
            id="navbar">
            <div class="cnt font-bold flex flex-col items-center">
                <span
                    class="w-[130px] h-[130px] rounded-full bg-white text-4xl block flex justify-center items-center border border-black">BC</span>
                <span class="text-2xl">Best Computer's</span>
            </div>
            <div class="cnt">
                <div>
                    <a href="/">Home</a>
                    <a href="">Availabel Stock</a>
                    <a href="">Sold Stock</a>
                    <a href="./issue.php">Issue</a>
                </div>
            </div>
        </nav>

        <!-- Main section -->
        <main class="lg:ml-[300px]">
            <div class="search flex justify-center items-center py-[1rem]">
                <input type="search" name="search" placeholder="Search"
                    class="md:w-[60%] w-full text-xl font-semibold rounded-lg">
            </div>
            <h1 class="text-4xl text-center my-8">Add product</h1>
            <div class="w-[90%] m-auto">
                <form method="post" enctype="multipart/form-data" class="form">
                    <div class="grid grid-cols-2 place-items-center">
                        <div class="inside-cnt">
                            Serial Number: <br> <input type="text" name="serial_no" placeholder="Serial Number" required
                                class="inputs">
                        </div>
                        <div>
                            Purchase Date: <br> <input type="text" name="date" placeholder="Purchase Date" required
                                class="inputs">
                        </div>
                        <div>
                            Company Name: <br> <input type="text" name="company_name" placeholder="Company Name"
                                required class="inputs">
                        </div>
                        <div>
                            Model Name: <br> <input type="text" name="model_name" placeholder="Model Name" required
                                class="inputs">
                        </div>
                        <div>
                            Processor: <br> <input type="text" name="processor" placeholder="Processor" required
                                class="inputs">
                        </div>
                        <div>
                            SSD: <br> <input type="text" name="ssd" placeholder="SSD" class="inputs">
                        </div>
                        <div>
                            HDD: <br> <input type="text" name="hdd" placeholder="HDD" class="inputs">
                        </div>
                        <div>
                            RAM: <br> <input type="text" name="ram" placeholder="RAM" required class="inputs">
                        </div>
                        <div>
                            Supplier Name: <br> <input type="text" name="supplier" placeholder="Supplier Name" required
                                class="inputs">
                        </div>
                        <div>
                            Device Available at: <br> <input type="text" name="available_at"
                                placeholder="Device Available at" required class="inputs">
                        </div>
                    </div>
                    <div class="my-4 mx-[3rem]">
                        Device Proof: <input type="file" name="device" accept="image/*" required><br><br>
                        Image Proof: <input type="file" name="image_proof" accept="image/*" required>
                    </div>
                    <div class="container-2 text-2xl border-1 border-black w-[200px] mx-[3rem] p-1 text-center rounded-[10px] bg-green-500 text-white">
                        <input type="submit" value="Submit Product" class="inputs-button">
                    </div>
                    <div class="container-2 text-2xl border-1 border-black w-[100px] mx-[3rem] p-1 text-center rounded-[10px]">
                        <input type="cancel" value="Cancel" class="">
                    </div>
            </div>

            </form>
    </div>
    </main>

    </div>
    <!-- <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" -->
    <!-- 	integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" -->
    <!-- 	crossorigin="anonymous"></script> -->
</body>

</html>