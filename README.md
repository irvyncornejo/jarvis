# jarvis -> Iza
Proyecto para generar acciones mediante comandos de voz. 
Implementando raspberry pi, chimalli y firebase

## Conectar con bocina Bluethoot
        systemctl is-enabled bluetooth.service
        bluetoothctl
        power on
        agent on
        scan on
        pair <F3:16:E9:1E:CC:5B>
        trust  <F3:16:E9:1E:CC:5B>
        paired-devices
        connect <F3:16:E9:1E:CC:5B>