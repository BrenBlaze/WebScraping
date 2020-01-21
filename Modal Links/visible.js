
//if else statement to show/hide the window. if visible, modalClass will have the display of block, go into the if, and get hidden

if($('.modalClass').css('display')=='block'){
	$('.modalClass').hide();
}
else if($('.modalClass').css('display')=='none'){
		$('.modalClass').show();
		}