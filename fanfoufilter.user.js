// ==UserScript==
// @name           Fanfou Filter
// @description    Filtering unwanted messages, and save your time
// @copyright      
// @license        GPL version 3 or later; http://www.gnu.org/copyleft/gpl.html
// @include        http://fanfou.com/* 
// @namespace      Rex Zhasm (http://fanfou.com/zhasm)
// @version        0.0.0.2
// history:        0.0.0.2:  

// ==/UserScript==


var g_keywords="轮功,"; // you may add your own ',' separeted keywords;
var g_sources="街旁,";    

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
loadJS('http://code.jquery.com/jquery-1.4.4.min.js'); 

// Check if jQuery's loaded
function GM_wait() {
    if(typeof unsafeWindow.jQuery == 'undefined') { 
        window.setTimeout(GM_wait,100); 
    }
    else { $ = unsafeWindow.jQuery; letsJQuery(); }
}

GM_wait();

function str2regex(s)
{
    //'abc,xyz'=> /abc|xyz/i

    var s=s.trim().split(",").join("|");
    return eval("/"+s+"/"); 
}

function filter(k, s)
{
    //filter content that is matched regex k
    //and source that is matched by regex s
    $(".content").each(function(){
        var content='*#$'+$(this).html();
        var result=content.search(k);
        result=parseInt(result);
        if ( result>0 ) // -1 means not found
        {
            $(this).parent().hide(); 
        }
    });
    $(".method").each(function(){
        var content="@#$"+$(this).html();
        var result=content.search(s);
        result=parseInt(result);
        if ( result >0 )
        {
            $(this).parent().parent().hide();//.parent().hide(); 
        }
    });

}

// All your GM code must be inside this function
function letsJQuery() {
    $.noConflict();
    //when loading the page, filter:
    var kr=str2regex(g_keywords);
    var sr=str2regex(g_sources);
    filter(kr, sr);

    $("#pagination-more, #timeline-notification").click(function(){
            setTimeout(function(){
                filter(kr, sr);
            }, 500);
    }); 
} 
