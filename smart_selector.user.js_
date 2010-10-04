// ==UserScript==
// @name           Smart Selector
// @description    select mids by using Shift+MouseOver 
// @copyright      Sep. 2010 
// @license        GPL version 3 or later; http://www.gnu.org/copyleft/gpl.html
// @include        http*://corpus.ironport.com/search/classify*
// @namespace      Rex Zhang @ TOC  Shanghai 
// @version        0.0.0.2
// history:        0.0.0.2: 2010.09.18 21:22 

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
   $("*").keydown(function(event){
         
        if(event.keyCode=='16' || event.keyCode=='17')
        {
            $(".roweven, .rowodd").mouseover(function(){
                var id=$(this).attr("id");
                id=id.replace(/\D+/g,"");
                var checked=$("#checkbox_"+id).attr("checked");
                if (event.keyCode=='16' )
                {
                    $("#checkbox_"+id).attr("checked", "checked");
                    var cls=$("#msg_row_"+id).attr("class");
                    cls=cls.replace(/\s*selected\s*/ig,"");
                    $("#msg_row_"+id).attr("class",cls+" selected");
                }
                else
                {
                    $("#checkbox_"+id).attr("checked", "");
                    var cls=$("#msg_row_"+id).attr("class").replace(/selected/gi,"");
                    $("#msg_row_"+id).attr("class",cls);
                }
            });
         
        }
        else
        {
            $(".roweven, .rowodd").unbind("mouseover"); 
            //this here mean key
            $(this).keydown();
        }
    });
    $("*").keyup(function(){
        $(".roweven, .rowodd").unbind("mouseover");
    });
} 


