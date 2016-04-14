// creating a bogus player

/* 
	this is supposed to be the player html
	
	<a download='myfile' id='urlfile'> <button id='playbutton'>Play</button> </a>
*/

var textfile = null,
	 makeTextFile = function(url) {
	var data = new Blob([text], {type: 'text/plain'});
	if (textfile !== null) {
		window.URL.revokeObjectURL(textfile);
	}

	textfile = window.URL.createObjectURL(data);
	return textfile;
};

var playbutton = document.getElementById('playbutton');
playbutton.addEventListener ('click', function() {
	var link = document.URL;
	link.href= makeTextFile(link);
}, false);