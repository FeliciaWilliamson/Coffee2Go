% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>{{ message }}</h3>
<!-- Login form for current users -->
<form method="post" action="map">

<label for= "name">Username</label>
<input type="text" id="userName" name="userName">

<label for= "password">Password</label>
<input type="text" id="password" name="password"><br>

<button type="button">Submit</button>

</form>


