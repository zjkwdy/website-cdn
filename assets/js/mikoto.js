function includeCss(filename) {
    var head = document.getElementsByTagName('head')[0];
    var link = document.createElement('link');
    link.href = filename;
    link.rel = 'stylesheet';
    link.type = 'text/css';
    head.appendChild(link)
}
for (i in document.getElementsByClassName('list-item')[0]["children"]) {
    try{
        document.getElementsByClassName('list-item')[0]["children"][i]["children"][0].innerHTML = '御坂妹妹真的太可爱啦！！' 
    }catch{
        console.log('1')
    }
}
for (i in document.getElementsByClassName('avatar')) {
    try{
        document.getElementsByClassName('avatar')[i].src='https://cdn.jsdelivr.net/gh/zjkwdy/website-cdn/assets/images/testboder.png'
    }catch{
        console.log('1')
    }
}
for (i in document.getElementsByClassName('name')) {
    try{
        document.getElementsByClassName('name')[i].innerHTML='御坂'+Math.floor(Math.random()*20000+3).toString(10)+'号'
    }catch{
        console.log('1')
    }
}