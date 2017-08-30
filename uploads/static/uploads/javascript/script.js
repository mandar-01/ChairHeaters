make_elements();
//insert_data();

// function make_elements(){
// 	//console.log(title.length);
// 	for(var i=0;i<3;i++){
// 		console.log("into js");
// 		var div = document.createElement("div");

// 		 var Title = title[i];
// 		 var Desc = desc[i];
// 		 var Name = username[i];

// 		div.className = "card mb-4";
// 		div.innerHTML = '<div class="card-block"><h2 class="card-title">Title</h2><p class="card-text"></p><a href="#" class="btn btn-primary">Read More &rarr;</a></div><div class="card-footer text-muted">Posted on January 1, 2017 by <a href="#"></a></div>';
// 		var element = document.getElementById("list");
// 		element.appendChild(div);
// 	}
// }

function make_elements(){
	//console.log(title.length);
	let array = [];
	for(var i=0;i<title.length;i++){
		console.log("into js");

		 var Title = title[i];
		 var Desc = desc[i];
		 var Name = username[i];
		let y1 = `<div class="card mb-4"><div class="card-block"><h2 class="card-title">${Title}</h2><p class="card-text"></p><a href="#" class="btn btn-primary">Read More &rarr;</a></div><div class="card-footer text-muted">Posted on January 1, 2017 by <a href="#"></a></div></div>`;
		array.push(y1);
		console.log("loop "+i);
		console.log(array);
		document.getElementById('list').innerHTML = array;
	}
}


// function insert_data(){
// 	for(var i=0;i<title.length;i++){
// 		document.getElementById("title"+"i").innerHTML = title[i];
// 	}
// }