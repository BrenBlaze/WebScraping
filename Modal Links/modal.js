$('#modalId').click(function(){
	$('.modalClass').css('display', 'none');
	
});



var modal = document.createElement("div");      //Creates the modal

var modalText = document.createElement("div"); //Modal Body
    modalText.style.position = "relative";
    
var span = document.createElement("span");   //close window button
    span.innerHTML = "&times;";
    
var par = document.createElement("p");      //Modal Text
    par.style.position = "relative";
    
var ul = document.createElement("ul");      //Starts List
    ul.style.position = "relative";
    
var li = document.createElement("li");      //List items
	li.style.position = "relative";

// text nodes and id/classes
document.body.prepend(modal);           //Add to the top of the documents body

var textNode = document.createTextNode("");     //Area for text

var modalId = document.createAttribute("id");       //Create the modal an id of modalId
modalId.value = "modalId";

var modalClass = document.createAttribute("class");     //Create the modal a class of modalClass
modalClass.value = "modalClass";


var modalContent = document.createAttribute("class");       //Give the text area of the modal the class modalContent
modalContent.value = "modalContent";


var spanClose = document.createAttribute("class");
spanClose.value = "closex";                                 //Give the span the class closex as I didn't know if close was a reserved word


modal.appendChild(textNode);                //Moves the text node inside the modal tags, if this were in HTML
modal.setAttributeNode(modalId);            //Sets the modal's ID to modalId
modal.setAttributeNode(modalClass);         // Sets the modal's class to modalClass
modalText.setAttributeNode(modalContent);   //stes the ModalText div to have the class modalContent
span.setAttributeNode(spanClose);           //Gives the span the class that has that weird symbol


modal.appendChild(modalText); //puts the modalText within the modal tags

modalText.appendChild(span); //puts the span, parargraph, and list tags inside of the modalText which is within the modal. 
modalText.appendChild(par);
modalText.appendChild(ul);


var anchors = document.getElementsByTagName('a');  //stores all elements with the anchor tag


var urllist = [];                                   //empty object to store href list in

for(var i=0; i < anchors.length; i++){              //cycle through anchor list elements
  //  alert(anchors[i].innerHTML);
 
    if (anchors[i].href != "") {
        var temp = anchors[i].attributes.href.textContent;
        if(temp.charAt(0)!= '/' && temp.charAt(0) != '#'){ //check to see if the first charachter is a '/'
            urllist.push(anchors[i].href);                     //if not, add to list
        }
    }
}

for(var i=0; i<urllist.length;i++){
	
	ul.append(urllist[i]+"\n\n\n");
	
}

// get all hrefs
var modal = document.getElementById('modalId');

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("closex")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
