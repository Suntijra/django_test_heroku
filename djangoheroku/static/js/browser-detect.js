function browserDetect(){
    var agent = navigator.userAgent;
    //alert(agent)
    console.log(agent.search('Edge'))
    if (agent.search('Edge') >=0){
        return "Edge";
    }else if(agent.search('Chorme') >=0){
        return 'Chorme';
    }
}
function plus(x,y){
    result = x+y;
    return result
}