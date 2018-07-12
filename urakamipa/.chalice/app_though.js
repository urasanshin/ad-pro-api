var xmlHttp;

xmlHttp = new XMLHttpRequest();
xmlHttp.open("GET", "https://vb38rgfmql.execute-api.ap-northeast-1.amazonaws.com/api/", false);
xmlHttp.send(null);
alert(xmlHttp.responseText);
