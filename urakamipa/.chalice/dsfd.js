$(function () {
    $('#ajax-button').click(
        function () {
            $.ajax({
                type:"get",
                url: 'https://vb38rgfmql.execute-api.ap-northeast-1.amazonaws.com/api/',
                dataType: ''
            }).done(function (data) {
                var message = jsonParser(data);
                $('results').html(message);
            }).fail(function (data) {
                $('#sample-results').html('<font color="red">読み込みNG(ChromeではNG)</font>');
            })
        }
    );
});