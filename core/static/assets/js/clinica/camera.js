
class Camera {
    constructor() {
        this.video = document.getElementById('video');
        this.canvas = document.getElementById('canvas');
        this.context = canvas.getContext('2d');
        this.errorMsgElement = document.querySelector('span#errorMsg');
        this.imageObj = new Image();
        this.stream = null;
        this.constraints = {
            audio: false,
            video: { width: 2500, height: 2500 }
        };
        this.imageObj.onload = function() {
            this.context.drawImage(this.imageObj, 5, 5, 250 + 50, 150);
        };
    }

    async iniciar(){
        try {
            this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
            this.stream = await navigator.mediaDevices.getUserMedia(this.constraints);
            window.stream = this.stream;
            this.video.srcObject = this.stream;
        } catch (e) {
            this.errorMsgElement.innerHTML = 'navigator.getUserMedia error:${e.toString()}';
        }
    }

    desativar(){
        this.stream.getTracks()[0].stop();
        this.context.restore();
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }

    capturar(id){
        this.context.restore();
        this.context.drawImage(this.video, 5, 5, 240 + 50, 140);
        //$(id).val(this.canvas.toDataURL());
    }

    carregarImagem(strDataURI) {
        "use strict";
        var img = new window.Image();
        img.addEventListener("load", function () {
            document.getElementById('canvas').getContext("2d").drawImage(img, 5, 5, 250 + 50, 150);
        });
        img.setAttribute("src", strDataURI);
    }
}