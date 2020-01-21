// To inject jQuery into 

//chrome.tabs.onUpdated.addListener(function(tab) {
chrome.browserAction.onClicked.addListener(function(tab) {

     // inject jQuery, then execute hide.js on callback
     chrome.tabs.executeScript({
        file: 'jquery-3.3.1.min.js'
            }, function(x) {                   // callback function (parameter is required) 
                    chrome.tabs.executeScript({
                        file: "visible.js" 
                    });
     });

     // insert CSS 
     chrome.tabs.insertCSS({
        file: "style.css"
     });
});
