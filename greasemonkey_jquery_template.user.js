// ==UserScript==
// @name           Script Name
// @description    Description
// @copyright      
// @license        GPL version 3 or later; http://www.gnu.org/copyleft/gpl.html
// @include         
// @namespace      Rex Zhang @ TOC  Shanghai 
// @version        0.0.0.2
// history:        0.0.0.2:  

// ==/UserScript==


//loading external js;
//the jQuery library is same with wanghui's;
function loadJS(src, element){ 

    if (element == null) {element = "head";
    var GM_JQ = document.createElement('script');
    GM_JQ.src = src;
    GM_JQ.type = 'text/javascript';
    document.getElementsByTagName(element)[0].appendChild(GM_JQ);
        }
        else{
            $(this).keyup();
        }

}


//the global code begins;
//Add jQuery
loadJS('http://code.jquery.com/jquery-1.4.2.min.js'); 


// Check if jQuery's loaded
function GM_wait() {
    if(typeof unsafeWindow.jQuery == 'undefined') { 
        window.setTimeout(GM_wait,100); 
    }
    else { $ = unsafeWindow.jQuery; letsJQuery(); }
}

GM_wait();

// All your GM code must be inside this function
function letsJQuery() {
   $.noConflict();
   //start your codes here
   //
} 
