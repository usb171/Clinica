$.ajax({
    url: "/core/getDataHoraAjax",
    dataType: 'json',
    success: function (data) {
        var started_at = new Date().getTime();
        var server_time = data.dataHora;
        function az(i) {if (i<10) {i = "0" + i};return i;}
        var clockInterval = setInterval(function(){
          var current_time = new Date().getTime();
          var excecution_time = parseInt((current_time - started_at) / 1000);
          var s = new Date((server_time + excecution_time) * 1000);
          dataHora = az(s.getDate())+'/'+az(s.getMonth()+1)+'/'+s.getFullYear()+'  '+az(s.getHours())+':'+az(s.getMinutes())+':'+az(s.getSeconds());
          $("#id_dataHora a").text(dataHora);
        }, 1000)
    }
});