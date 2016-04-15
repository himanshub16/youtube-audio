// Here You can type your custom JavaScript...function saveTextAsFile()
	{
		// var textToWrite = document.getElementById("inputTextToSave").value;
		var textToWrite = document.URL;
		var textFileAsBlob = new Blob([textToWrite], {type:'html'});
		var fileNameToSaveAs = "myfile";

		var downloadLink = document.createElement("a");
		downloadLink.download = fileNameToSaveAs;
		downloadLink.innerHTML = "Download File";
		if (window.URL != null)
		{
			// Chrome allows the link to be clicked
			// without actually adding it to the DOM.
			downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
		}
		else
		{
			// Firefox requires the link to be added to the DOM
			// before it can be clicked.
			downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
			downloadLink.onclick = destroyClickedElement;
			downloadLink.style.display = "none";
			document.body.appendChild(downloadLink);
		}

		downloadLink.click();

		// create player once things have been done, and remove the button
		// document.getElementById('playbutton').remove();
		// document.getElementById('myaudioplayer').innerHTML = 
	}

	function destroyClickedElement(event)
	{
		document.body.removeChild(event.target);
	}
	
	var elem = document.getElementById('yt-masthead-content');
	var myhtml = '<button id="playbutton" style="width: 200px; " onclick="saveTextAsFile()">Stream audio</button>';
	elem.insertAdjacentHTML('beforeBegin', myhtml);
	document.getElementById('player-mole-container').remove();
	document.getElementById('placeholder-player').remove()