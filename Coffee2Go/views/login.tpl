
% rebase('layout.tpl', title=title, year=year)


<h2>{{ title }}.</h2>
<h3>{{ message }}</h3>
<!-- Login form for current users, when submit button is selected the user is redirected to the map.html page.-->
<body>
<!--Changed the method to GET, and the directed page in action. -->
<form method="GET"  action="/error">

<label for= "name">Username</label>
<input type="text" id="userName" name="userName">

<label for= "password">Password</label>
<input type="text" id="password" name="password"><br>

<button type="submit" value='submit'>Submit</button>

</form>
</body>

