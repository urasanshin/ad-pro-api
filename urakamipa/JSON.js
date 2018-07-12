var xmlHttpRequest = new XMLHttpRequest();
xmlHttpRequest.onreadystatechange = function()
{
    if( this.readyState == 4 && this.status == 200 )
    {
        if( this.response )
        {
            console.log(this.response);
            // 読み込んだ後処理したい内容をかく

        }
    }
}

xmlHttpRequest.open( 'GET', 'https://vb38rgfmql.execute-api.ap-northeast-1.amazonaws.com/api/', true );
xmlHttpRequest.responseType = 'json';
xmlHttpRequest.send( null );