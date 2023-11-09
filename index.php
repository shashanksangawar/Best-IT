<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title></title>
<style>
body{
  font-size: 25px;
}
.main_container{
  width: 100%;
  height: 90dvh;
  display: flex;
  gap: 2rem;
}
.box{
  width: 100%;
}
.grid{
  display: grid;
  grid-template-columns: auto auto auto;
  gap: 1rem;
}
.grid > input{
  width: 90%;
  height: 40px;
}
nav{
  display: flex;
  justify-content: space-between;
  padding: 10px 30px;
  border-bottom: 1px solid #000;
}
.SideNavbar{
  width: 20%; 
  border-bottom: 1px solid #000;
}
.search_box{
  width: 60dvh;
  height: 30px;
}
.btn > button{
  padding: 0.8rem;
  font-size: 20px;
}
</style>
</head>
<body>
    <nav>
      <span>Best Computer</span>
      <input type="text" placeholder="Search" class="search_box">
    </nav>
  <div class="main_container">
    <div class="SideNavbar">     
      <div class="nav-items">Add stock</div>
      <div class="nav-items">Available stock</div>
      <div class="nav-items">Sold stock</div>
      <div class="nav-items">Issue</div>
      <div class="nav-items">Breaked</div>
    </div>
    <div class="box">
      <form action="">
      <fieldset>
        <legend>Product</legend>
      <div class="grid">
        <input type="text">
        <input type="text">
        <input type="text">
        <input type="text">
        <input type="text">
        <input type="text">
        <input type="text">
        <input type="text">
        <input type="text">
        <input type="text">
      </div>
      </fieldset>
        <div class="btn">
          <button>Submit</button>
          <button>Cancel</button>
        </div>
      </form>
    </div>
  </div>
</body>
</html>

<?php 
?>
