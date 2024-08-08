$(document).ready(function(){
    function translate() {
        const lang = $('#language_code').val();
        $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: lang }, function(data){
            $('#hello').text(data.hello);
        });
    }

    $('#btn_translate').click(translate);
    $('#language_code').keypress(function(event){
        if (event.keyCode === 13) {
            translate();
        }
    });
});
