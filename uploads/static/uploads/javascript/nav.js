navbar();
function navbar(){
	document.getElementById('nav').innerHTML = ' <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarExample" aria-controls="navbarExample" aria-expanded="false" aria-label="Toggle navigation">'+
            '<span class="navbar-toggler-icon"></span>'+
        '</button>'+
        '<div class="container">'+
         '<a class="navbar-brand" href="#">ChairHeaters</a>'+
            '<div class="collapse navbar-collapse" id="navbarExample">'+
                '<ul class="navbar-nav ml-auto">'+
                    '<li class="nav-item active">'+
                        '<a class="nav-link" href="/uploads/">Home <span class="sr-only">(current)</span></a>'+
                    '</li>'+
                    '<li class="nav-item">'+
                        '<a class="nav-link" href="#">About</a>'+
                    '</li>'+
                    '<li class="nav-item">'+
                        '<a class="nav-link" href="/uploads/create/">New Post</a>'+
                    '</li>'+
                    '<li class="nav-item">'+
                        '<a class="nav-link" href="#">Contact</a>'+
                    '</li>'+
                '</ul>'+
            '</div>'+
        '</div>';
}